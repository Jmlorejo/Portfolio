"""Generate static HTML for GitHub Pages from the Flask templates.

Usage:
    python generate_static.py

This script starts the Flask app in test mode, fetches the root endpoint (and any
additional endpoints if needed) and writes the resulting HTML to the `docs/`
directory.  Committing the contents of `docs/` updates the GitHub Pages site.
"""

import os

from app import app


def write_file(filename: str, content: str) -> None:
    path = os.path.join(os.getcwd(), "docs", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    with app.test_client() as client:
        # fetch index and write to docs/index.html
        resp = client.get("/")
        if resp.status_code == 200:
            write_file("index.html", resp.data.decode("utf-8"))
            print("Wrote docs/index.html")
        else:
            print("Failed to render /, status", resp.status_code)

        # optionally render sections if you want separate files
        sections = ["about", "experience", "skills", "achievements"]
        for sec in sections:
            resp = client.get(f"/section/{sec}")
            if resp.status_code == 200:
                write_file(f"{sec}.html", resp.data.decode("utf-8"))
                print(f"Wrote docs/{sec}.html")
            else:
                print(f"Failed to render section {sec}, status", resp.status_code)

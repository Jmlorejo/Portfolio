# John Mark Lorejo - Portfolio

Personal portfolio website showcasing my experience as a NOC Engineer specializing in MSP and Web3 environments.

## Features

- Modern, responsive design with black & white theme
- Animated typing effect for hero section
- Floating particle background animations
- Scroll-reveal animations for sections
- Glassmorphism UI elements
- Social media integration (GitHub, LinkedIn, Facebook)

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Fonts**: Google Fonts (Inter, Space Grotesk)
- **Animations**: CSS Keyframes, Intersection Observer API

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Jmlorejo/portfolio.git
cd portfolio
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application locally (useful for previewing changes):
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5001
```

### Static site generation

This project uses GitHub Pages to host the public website (https://jmlorejo.github.io/Portfolio/).
The Pages service can only serve static files, so you must regenerate the
`docs/` folder whenever the Flask templates or data change. A helper script is
included to automate this:

```bash
python generate_static.py
``` 

Running the script will render the app’s routes and write the resulting HTML
into `docs/`. Commit and push the updated `docs/` files and Pages will publish
the new content.

> **Tip:** a GitHub Action is included (`.github/workflows/static.yml`) that
> automatically regenerates and commits `docs/` on every push to `main`, so you
don't have to run the script manually unless you want to preview changes locally.

## Structure

```
Portfolio/
├── app.py              # Flask application
├── static/             # Static assets
│   └── profile.jpg     # Profile image
├── templates/          # HTML templates
│   ├── index.html      # Main template
│   └── sections/       # Section templates
│       ├── about.html
│       ├── experience.html
│       ├── skills.html
│       └── achievements.html
└── README.md
```

## Contact

- Email: jmlorejo013@gmail.com
- Phone: +63 951 146 1981
- Location: Rizal, Philippines

## License

© 2025 John Mark Lorejo. All rights reserved.

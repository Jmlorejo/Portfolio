param(
    [string]$VenvName = ".venv"
)

if (-not (Get-Command python -ErrorAction SilentlyContinue) -and -not (Get-Command py -ErrorAction SilentlyContinue)) {
    Write-Error "Python not found on PATH. Install Python from https://python.org and enable 'Add to PATH'."
    exit 1
}

$python = if (Get-Command py -ErrorAction SilentlyContinue) { "py -3" } else { "python" }

if (!(Test-Path $VenvName)) {
    & $python -m venv $VenvName
}

# Activate the venv for the current session (PowerShell)
$activate = "$VenvName\Scripts\Activate.ps1"
if (Test-Path $activate) {
    Write-Output "Activating virtual environment: $activate"
    & $activate
}

& $python -m pip install --upgrade pip
& $python -m pip install -r requirements.txt

Write-Output "Setup complete. Activate later with: $VenvName\Scripts\Activate.ps1"
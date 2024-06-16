import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of packages to be installed
packages = [
    "discord",
    "pynput",
    "pyautogui",
    "Pillow",          # PIL is part of the Pillow package
    "python-dotenv"
]

# Install each package
for package in packages:
    try:
        install(package)
        print(f"Successfully installed {package}")
    except Exception as e:
        print(f"Error installing {package}: {e}")

print("All packages installed.")

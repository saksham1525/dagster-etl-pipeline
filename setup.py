#!/usr/bin/env python3

import subprocess
import sys
import os

def setup_environment():
    """Create virtual environment and install dependencies."""
    
    # Check Python version
    if sys.version_info < (3, 9) or sys.version_info >= (3, 13):
        print(f"Error: Python 3.9-3.12 required. Found: {sys.version_info.major}.{sys.version_info.minor}")
        sys.exit(1)
    
    # Create virtual environment
    print("Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    
    # Activate and install dependencies
    venv_python = os.path.join("venv", "bin", "python") if os.name != 'nt' else os.path.join("venv", "Scripts", "python.exe")
    
    print("Installing dependencies...")
    subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"], check=True, capture_output=True)
    subprocess.run([venv_python, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    
    # Create data directories
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/staging", exist_ok=True) 
    os.makedirs("data/outputs", exist_ok=True)
    
    print("\nSetup complete.")
    print(f"Activate environment: source venv/bin/activate")
    print(f"Start Dagster: dagster dev")

if __name__ == "__main__":
    setup_environment()

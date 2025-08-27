#!/usr/bin/env python3
"""
Setup script for Fizzy's Autoclicker development environment
"""

import os
import sys
import subprocess
import venv

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return False

def setup_environment():
    """Set up the development environment"""
    print("🚀 Setting up Fizzy's Autoclicker development environment...\n")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ is required!")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Create virtual environment
    if not os.path.exists('.venv'):
        print("🔄 Creating virtual environment...")
        venv.create('.venv', with_pip=True)
        print("✅ Virtual environment created!")
    else:
        print("✅ Virtual environment already exists!")
    
    # Determine activation command based on OS
    if os.name == 'nt':  # Windows
        activate_cmd = r'.venv\Scripts\activate.bat && '
        pip_cmd = r'.venv\Scripts\pip.exe'
    else:  # Linux/Mac
        activate_cmd = 'source .venv/bin/activate && '
        pip_cmd = '.venv/bin/pip'
    
    # Install dependencies
    if not run_command(f'{pip_cmd} install -r requirements.txt', 
                      'Installing dependencies'):
        return False
    
    # Test installation
    if not run_command(f'{activate_cmd}python -c "import customtkinter; import pynput; print(\'All dependencies installed correctly!\')"',
                      'Testing installation'):
        return False
    
    print("\n🎉 Setup completed successfully!")
    print("\n📝 Next steps:")
    print("1. Activate the virtual environment:")
    if os.name == 'nt':
        print("   .venv\\Scripts\\activate")
    else:
        print("   source .venv/bin/activate")
    print("2. Run the application:")
    print("   python autoclicker.py")
    print("3. Build executable:")
    print("   pyinstaller --onefile --windowed --name FizzysAutoclicker autoclicker.py")
    print("\n📖 See CONTRIBUTING.md for more details!")
    
    return True

if __name__ == "__main__":
    if setup_environment():
        sys.exit(0)
    else:
        sys.exit(1)

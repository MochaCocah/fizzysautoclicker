# ✨ Fizzy's Autoclicker

A modern, stylish GUI auto clicker application built with Python and CustomTkinter.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Built with CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blue.svg)](https://github.com/TomSchimansky/CustomTkinter)

> **⚠️ Disclaimer**: This tool is for educational and personal use only. Please use responsibly and respect the terms of service of other applications.

## 📸 Screenshots

*Coming soon - we'll add screenshots of the application in action!*

## 🚀 Quick Start (Standalone Executable)

**No Python installation required!**

1. Download or navigate to the `dist` folder
2. Run `FizzysAutoclicker.exe` 
3. The application will start immediately!

Alternative: Use the `launch.bat` file for quick launching.

## � Developer Installation

If you want to run from source or modify the code:

1. Make sure you have Python 3.7+ installed
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Building Executable

To build your own executable:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run the build command:
   ```bash
   pyinstaller --onefile --windowed --name "FizzysAutoclicker" autoclicker.py
   ```

3. The executable will be created in the `dist` folder

## Features

- 🎨 **Modern UI**: Built with CustomTkinter for a sleek, modern appearance
- 🌙 **Dark/Light Theme**: Toggle between dark and light modes
- ⚡ **Customizable Settings**: Adjust click interval, click type, and repeat count
- 🎯 **Flexible Targeting**: Click at cursor position or custom coordinates
- ⌨️ **Hotkey Support**: Use F6 to start/stop clicking from anywhere
- 📊 **Real-time Counter**: Track the number of clicks performed
- 💾 **Settings Persistence**: Automatically saves and loads your preferences
- 🔝 **Always on Top**: Optional always-on-top window mode
- 📦 **Standalone Executable**: No Python required - runs anywhere on Windows!

## Executable Information

- **File**: `dist/ModernAutoClicker.exe`
- **Size**: ~13 MB (includes all dependencies)
- **Requirements**: Windows 7/8/10/11 (64-bit)
- **No installation needed** - just run the .exe file!

## Usage

1. Run the application:
   ```bash
   python autoclicker.py
   ```

2. Configure your settings:
   - **Click Interval**: Time between clicks in seconds
   - **Click Type**: Left, right, or middle mouse button
   - **Repeat Count**: Number of clicks (0 = infinite)
   - **Target Location**: Current cursor or custom position

3. Start clicking:
   - Click the "Start Clicking" button
   - Or press F6 hotkey from anywhere on your system

4. Stop clicking:
   - Click the "Stop Clicking" button
   - Or press F6 again

## Requirements

- Python 3.7+
- customtkinter
- pynput
- Pillow
- packaging

## Features Overview

### Modern Interface
- Clean, responsive design with rounded corners
- Smooth animations and visual feedback
- Intuitive layout with organized sections

### Flexible Configuration
- Adjustable click intervals (supports decimal values)
- Multiple click types (left, right, middle button)
- Custom target positioning with visual capture tool
- Repeat count settings for precise automation

### Advanced Features
- Hotkey support for system-wide control
- Settings persistence across sessions
- Theme switching (dark/light mode)
- Always-on-top window option
- Real-time click counter

## Safety Notes

- Use responsibly and in accordance with software terms of service
- Be mindful of click intervals to avoid overwhelming target applications
- The application includes safety features like hotkey stopping

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Quick Contribution Ideas
- 🐛 Report bugs
- 💡 Suggest new features  
- 📖 Improve documentation
- 🎨 Design improvements
- 🧪 Add tests
- 🌍 Translations

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔒 Security

Please review our [Security Policy](SECURITY.md) for reporting vulnerabilities.

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed list of changes and versions.

## 🙏 Acknowledgments

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - For the modern UI framework
- [pynput](https://github.com/moses-palmer/pynput) - For cross-platform input control
- [PyInstaller](https://github.com/pyinstaller/pyinstaller) - For executable creation

## ⭐ Star History

If you find this project useful, please consider giving it a star! ⭐

---

**Happy Clicking!** 🖱️✨

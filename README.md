# Fizzy's Autoclicker

A sleek modernize auto clicker, (not a competitor for OG Auto Clicker.) At least mines open source, lmao- *says the hundreds of auto clickers on github*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Built with CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blue.svg)](https://github.com/TomSchimansky/CustomTkinter)



## Why I Built This

I dunno, guess a little side project because I don't got nothing else to do in my life 🤷‍♂️

## Download & Run

**Just want to use it?** Grab the executable from the [releases page](https://github.com/MochaCocah/fizzysautoclicker/releases) and run it. No Python installation needed.

1. Download `FizzysAutoclicker.exe` 
2. Run it
3. That's pretty much it, cuh. 

You can also use the `launch.bat` file if you're into that sort of thing, *psychopath...*

## What It Does

### The Good Stuff
- **Actually looks good** - Dark/light themes, rounded corners, smooth animations
- **Click where you want** - Current cursor position or set custom coordinates  
- **Hotkey control** - Press F6 from anywhere to start/stop (or set your own hotkeys :3)
- **Flexible timing** - Set any interval you want (even decimals like 0.5 seconds)
- **Multiple click types** - Left, right, or middle mouse button (don't know why I added all 3, but whatever I guess.)
- **Smart repeat counts** - Set a specific number or let it run forever
- **Remembers your settings** - No need to reconfigure every time
- **Stay on top mode** - Keep the window visible while using other apps

### The Technical Stuff
- Built with CustomTkinter for that modern look
- Real-time click counter with animations
- Position capture tool for easy coordinate selection
- Settings persistence across sessions
- Standalone executable (no dependencies to install)

## Running from Source

Want to build it from source because you're a gay
little nerd?

```bash
git clone https://github.com/MochaCocah/fizzysautoclicker.git
cd fizzysautoclicker
pip install -r requirements.txt
python autoclicker.py
```

## Building Your Own Executable

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "FizzysAutoclicker" autoclicker.py
```

The executable will be in the `dist` folder.

## How to Use

1. **Set your click speed** - Anything from 0.1 seconds to whatever you want
2. **Choose your target** - Either where your mouse is now, or click "Capture" to pick a spot
3. **Pick your click type** - Left, right, or middle mouse button
4. **Set repeat count** - Leave it at 0 for infinite clicking, or set a specific number
5. **Hit Start** or press F6 from anywhere on your computer
6. **Press F6 again to stop** (or click the stop button)

## Safety Notes

Look, auto clickers can be powerful tools, so use them responsibly:
- Don't overwhelm applications with super fast clicking
- The F6 hotkey works globally, so you can always stop it
- Be mindful of what you're clicking on

## Contributing

Found a bug? Want to add a feature? Check out the [contributing guidelines](CONTRIBUTING.md) to get started.

Some ideas for contributions:
 Literally none for now, it's A FUCKING AUTOCLICKER!
## License

MIT License - basically, do whatever you want with it, just don't blame me if something goes wrong.

## Acknowledgments

Thanks to the awesome developers who made this possible:
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - For making Python GUIs look actually modern
- [pynput](https://github.com/moses-palmer/pynput) - For handling all the mouse and keyboard stuff
- [PyInstaller](https://github.com/pyinstaller/pyinstaller) - For making it easy to share without Python

---

Happy ~~cheating~~ clicking! 


**NO AI WAS USE TO CREATE THIS GOD DAMN PROJECT, IM SMART, IM BETTER! GRAGHHHHHHH**
@echo off
echo Building Fizzy's Autoclicker executable...
echo.

REM Clean previous builds
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
if exist "*.spec" del "*.spec"

echo Compiling with PyInstaller...
pyinstaller --onefile --windowed --name "FizzysAutoclicker" --hidden-import "PIL._tkinter_finder" --hidden-import "tkinter" --hidden-import "customtkinter" --hidden-import "pynput" --clean autoclicker.py

echo.
if exist "dist\FizzysAutoclicker.exe" (
    echo SUCCESS: Executable created at dist\FizzysAutoclicker.exe
    echo File size:
    dir "dist\FizzysAutoclicker.exe" | find ".exe"
    echo.
    echo You can now run Fizzy's Autoclicker without Python installed!
) else (
    echo ERROR: Build failed. Check the output above for errors.
)

echo.
pause

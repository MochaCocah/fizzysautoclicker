import customtkinter as ctk
import threading
import time
from pynput import mouse, keyboard
from pynput.mouse import Button, Listener as MouseListener
from pynput.keyboard import Key, Listener as KeyboardListener
import json
import os
from tkinter import messagebox
import tkinter as tk

class ModernAutoClicker:
    def __init__(self):
        # Initialize variables
        self.clicking = False
        self.click_count = 0
        self.target_x = 0
        self.target_y = 0
        self.click_thread = None
        self.mouse_listener = None
        self.keyboard_listener = None
        self.hotkey_enabled = True
        
        # Settings
        self.settings = {
            "click_interval": 1.0,
            "click_type": "left",
            "repeat_count": 0,  # 0 = infinite
            "hotkey": "f6",
            "theme": "dark",
            "target_location": "cursor"
        }
        
        self.load_settings()
        self.setup_ui()
        self.setup_listeners()
        
    def setup_ui(self):
        # Set appearance mode and color theme
        ctk.set_appearance_mode(self.settings["theme"])
        ctk.set_default_color_theme("blue")
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("Fizzy's Autoclicker")
        self.root.geometry("450x600")
        self.root.resizable(False, False)
        
        # Set window icon and make it stay on top option
        self.root.attributes('-topmost', False)
        
        # Create main frame with padding
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=20)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title with animation effect
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="✨ Fizzy's Autoclicker",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=("gray10", "gray90")
        )
        self.title_label.pack(pady=(20, 30))
        
        # Status frame
        self.status_frame = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.status_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Status: Ready",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("green", "lightgreen")
        )
        self.status_label.pack(pady=15)
        
        self.click_counter = ctk.CTkLabel(
            self.status_frame,
            text="Clicks: 0",
            font=ctk.CTkFont(size=14)
        )
        self.click_counter.pack(pady=(0, 15))
        
        # Settings frame
        self.settings_frame = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.settings_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Click interval setting
        ctk.CTkLabel(
            self.settings_frame,
            text="Click Interval (seconds):",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w", padx=20, pady=(20, 5))
        
        self.interval_var = tk.StringVar(value=str(self.settings["click_interval"]))
        self.interval_entry = ctk.CTkEntry(
            self.settings_frame,
            textvariable=self.interval_var,
            width=100,
            height=35,
            corner_radius=10
        )
        self.interval_entry.pack(anchor="w", padx=20, pady=(0, 15))
        
        # Click type setting
        ctk.CTkLabel(
            self.settings_frame,
            text="Click Type:",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w", padx=20, pady=(0, 5))
        
        self.click_type_var = tk.StringVar(value=self.settings["click_type"])
        self.click_type_menu = ctk.CTkOptionMenu(
            self.settings_frame,
            values=["left", "right", "middle"],
            variable=self.click_type_var,
            width=150,
            height=35,
            corner_radius=10
        )
        self.click_type_menu.pack(anchor="w", padx=20, pady=(0, 15))
        
        # Repeat count setting
        ctk.CTkLabel(
            self.settings_frame,
            text="Repeat Count (0 = infinite):",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w", padx=20, pady=(0, 5))
        
        self.repeat_var = tk.StringVar(value=str(self.settings["repeat_count"]))
        self.repeat_entry = ctk.CTkEntry(
            self.settings_frame,
            textvariable=self.repeat_var,
            width=100,
            height=35,
            corner_radius=10
        )
        self.repeat_entry.pack(anchor="w", padx=20, pady=(0, 15))
        
        # Target location setting
        ctk.CTkLabel(
            self.settings_frame,
            text="Target Location:",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w", padx=20, pady=(0, 5))
        
        self.target_frame = ctk.CTkFrame(self.settings_frame, fg_color="transparent")
        self.target_frame.pack(anchor="w", padx=20, pady=(0, 20))
        
        self.target_var = tk.StringVar(value=self.settings["target_location"])
        self.cursor_radio = ctk.CTkRadioButton(
            self.target_frame,
            text="Current Cursor Position",
            variable=self.target_var,
            value="cursor"
        )
        self.cursor_radio.pack(anchor="w", pady=2)
        
        self.custom_radio = ctk.CTkRadioButton(
            self.target_frame,
            text="Custom Position",
            variable=self.target_var,
            value="custom"
        )
        self.custom_radio.pack(anchor="w", pady=2)
        
        # Position frame
        self.position_frame = ctk.CTkFrame(self.target_frame, fg_color="transparent")
        self.position_frame.pack(anchor="w", pady=(5, 0))
        
        ctk.CTkLabel(self.position_frame, text="X:").pack(side="left")
        self.x_var = tk.StringVar(value=str(self.target_x))
        self.x_entry = ctk.CTkEntry(self.position_frame, textvariable=self.x_var, width=80, height=30)
        self.x_entry.pack(side="left", padx=(5, 10))
        
        ctk.CTkLabel(self.position_frame, text="Y:").pack(side="left")
        self.y_var = tk.StringVar(value=str(self.target_y))
        self.y_entry = ctk.CTkEntry(self.position_frame, textvariable=self.y_var, width=80, height=30)
        self.y_entry.pack(side="left", padx=(5, 10))
        
        self.capture_btn = ctk.CTkButton(
            self.position_frame,
            text="Capture",
            command=self.capture_position,
            width=80,
            height=30,
            corner_radius=8
        )
        self.capture_btn.pack(side="left", padx=(5, 0))
        
        # Control buttons frame
        self.control_frame = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.control_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Start/Stop button with animation
        self.start_btn = ctk.CTkButton(
            self.control_frame,
            text="▶️ Start Clicking",
            command=self.toggle_clicking,
            width=200,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            corner_radius=15,
            fg_color=("green", "darkgreen"),
            hover_color=("darkgreen", "green")
        )
        self.start_btn.pack(pady=20)
        
        # Hotkey info
        self.hotkey_label = ctk.CTkLabel(
            self.control_frame,
            text=f"Hotkey: {self.settings['hotkey'].upper()} (Toggle)",
            font=ctk.CTkFont(size=12),
            text_color=("gray60", "gray40")
        )
        self.hotkey_label.pack(pady=(0, 10))
        
        # Footer frame with additional options
        self.footer_frame = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.footer_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Theme toggle
        self.theme_switch = ctk.CTkSwitch(
            self.footer_frame,
            text="Dark Mode",
            command=self.toggle_theme,
            onvalue="dark",
            offvalue="light"
        )
        self.theme_switch.pack(side="left", padx=20, pady=15)
        if self.settings["theme"] == "dark":
            self.theme_switch.select()
        
        # Always on top toggle
        self.topmost_switch = ctk.CTkSwitch(
            self.footer_frame,
            text="Always on Top",
            command=self.toggle_topmost
        )
        self.topmost_switch.pack(side="right", padx=20, pady=15)
        
        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def setup_listeners(self):
        """Setup keyboard and mouse listeners"""
        self.keyboard_listener = KeyboardListener(on_press=self.on_key_press)
        self.keyboard_listener.start()
        
    def on_key_press(self, key):
        """Handle keyboard events"""
        try:
            if hasattr(key, 'name') and key.name == self.settings["hotkey"]:
                if self.hotkey_enabled:
                    self.toggle_clicking()
            elif key == Key.f6 and self.settings["hotkey"] != "f6":
                if self.hotkey_enabled:
                    self.toggle_clicking()
        except AttributeError:
            pass
            
    def capture_position(self):
        """Capture current mouse position"""
        self.root.withdraw()  # Hide window
        messagebox.showinfo("Position Capture", "Click anywhere on the screen to capture position...")
        
        def on_click(x, y, button, pressed):
            if pressed:
                self.target_x = x
                self.target_y = y
                self.x_var.set(str(x))
                self.y_var.set(str(y))
                self.root.deiconify()  # Show window again
                return False  # Stop listener
                
        # Start mouse listener for position capture
        mouse_listener = MouseListener(on_click=on_click)
        mouse_listener.start()
        mouse_listener.join()
        
    def toggle_clicking(self):
        """Toggle the auto clicking on/off"""
        if not self.clicking:
            self.start_clicking()
        else:
            self.stop_clicking()
            
    def start_clicking(self):
        """Start the auto clicking process"""
        try:
            # Validate and update settings
            self.settings["click_interval"] = float(self.interval_var.get())
            self.settings["click_type"] = self.click_type_var.get()
            self.settings["repeat_count"] = int(self.repeat_var.get())
            self.settings["target_location"] = self.target_var.get()
            
            if self.settings["click_interval"] <= 0:
                messagebox.showerror("Error", "Click interval must be greater than 0!")
                return
                
            # Get target position
            if self.settings["target_location"] == "cursor":
                self.target_x, self.target_y = mouse.Controller().position
            else:
                self.target_x = int(self.x_var.get())
                self.target_y = int(self.y_var.get())
                
        except ValueError as e:
            messagebox.showerror("Error", "Please enter valid numeric values!")
            return
            
        self.clicking = True
        self.click_count = 0
        
        # Update UI
        self.start_btn.configure(
            text="⏹️ Stop Clicking",
            fg_color=("red", "darkred"),
            hover_color=("darkred", "red")
        )
        self.status_label.configure(
            text="Status: Clicking...",
            text_color=("red", "lightcoral")
        )
        
        # Start clicking thread
        self.click_thread = threading.Thread(target=self.click_worker)
        self.click_thread.daemon = True
        self.click_thread.start()
        
        # Animate status (optional visual feedback)
        self.animate_status()
        
    def stop_clicking(self):
        """Stop the auto clicking process"""
        self.clicking = False
        
        # Update UI
        self.start_btn.configure(
            text="▶️ Start Clicking",
            fg_color=("green", "darkgreen"),
            hover_color=("darkgreen", "green")
        )
        self.status_label.configure(
            text="Status: Stopped",
            text_color=("orange", "yellow")
        )
        
        # Save settings
        self.save_settings()
        
    def click_worker(self):
        """Worker thread for clicking"""
        mouse_controller = mouse.Controller()
        
        # Determine button type
        button_map = {
            "left": Button.left,
            "right": Button.right,
            "middle": Button.middle
        }
        button = button_map.get(self.settings["click_type"], Button.left)
        
        while self.clicking:
            # Perform click
            mouse_controller.position = (self.target_x, self.target_y)
            mouse_controller.click(button)
            
            self.click_count += 1
            
            # Update counter in main thread
            self.root.after(0, self.update_click_counter)
            
            # Check if we should stop (repeat count reached)
            if self.settings["repeat_count"] > 0 and self.click_count >= self.settings["repeat_count"]:
                self.root.after(0, self.stop_clicking)
                break
                
            # Wait for next click
            time.sleep(self.settings["click_interval"])
            
    def update_click_counter(self):
        """Update the click counter display"""
        self.click_counter.configure(text=f"Clicks: {self.click_count}")
        
    def animate_status(self):
        """Simple animation for status when clicking"""
        if self.clicking:
            current_text = self.status_label.cget("text")
            if "..." in current_text:
                dots = current_text.count(".")
                if dots >= 3:
                    new_text = "Status: Clicking"
                else:
                    new_text = current_text + "."
            else:
                new_text = current_text + "."
                
            self.status_label.configure(text=new_text)
            self.root.after(500, self.animate_status)
            
    def toggle_theme(self):
        """Toggle between light and dark themes"""
        new_theme = self.theme_switch.get()
        self.settings["theme"] = new_theme
        ctk.set_appearance_mode(new_theme)
        self.save_settings()
        
    def toggle_topmost(self):
        """Toggle always on top functionality"""
        self.root.attributes('-topmost', self.topmost_switch.get())
        
    def load_settings(self):
        """Load settings from file"""
        try:
            if os.path.exists("autoclicker_settings.json"):
                with open("autoclicker_settings.json", "r") as f:
                    saved_settings = json.load(f)
                    self.settings.update(saved_settings)
        except Exception:
            pass  # Use default settings if loading fails
            
    def save_settings(self):
        """Save current settings to file"""
        try:
            with open("autoclicker_settings.json", "w") as f:
                json.dump(self.settings, f, indent=2)
        except Exception:
            pass  # Fail silently if saving fails
            
    def on_closing(self):
        """Handle window closing"""
        self.clicking = False
        self.save_settings()
        
        # Stop listeners
        if self.keyboard_listener:
            self.keyboard_listener.stop()
            
        self.root.destroy()
        
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = ModernAutoClicker()
    app.run()

import tkinter as tk
from tkinter import messagebox

class MotoRentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Motorcycle Rental - Dark Mode Simulation")
        self.root.geometry("400x500")

        # Define themes
        self.themes = {
            "light": {
                "bg": "#ffffff",
                "fg": "#333333",
                "btn_bg": "#e0e0e0",
                "btn_fg": "#000000",
                "accent": "#ff9800",
                "card_bg": "#f5f5f5"
            },
            "dark": {
                "bg": "#121212",
                "fg": "#e0e0e0",
                "btn_bg": "#333333",
                "btn_fg": "#ffffff",
                "accent": "#ffa726",
                "card_bg": "#1e1e1e"
            }
        }

        self.current_theme = "light"

        # Initialize UI Components
        self.create_widgets()
        self.apply_theme()

    def create_widgets(self):
        # Header
        self.header_label = tk.Label(
            self.root, 
            text="🛵 Motorcycle Rental", 
            font=("Arial", 20, "bold"),
            pady=20
        )
        self.header_label.pack(fill=tk.X)

        # Rental Card (Simulated)
        self.card_frame = tk.Frame(self.root, padx=20, pady=20, relief=tk.RIDGE, borderwidth=1)
        self.card_frame.pack(pady=20, padx=20, fill=tk.BOTH)

        self.moto_name = tk.Label(
            self.card_frame, 
            text="Yamaha MT-07", 
            font=("Arial", 14, "bold")
        )
        self.moto_name.pack(anchor="w")

        self.moto_desc = tk.Label(
            self.card_frame, 
            text="Available for rent in Kyiv.\nPrice: 1500 UAH/day", 
            justify=tk.LEFT
        )
        self.moto_desc.pack(anchor="w", pady=10)

        self.rent_btn = tk.Button(
            self.card_frame, 
            text="Rent Now", 
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        self.rent_btn.pack(pady=10)

        # Theme Toggle Button
        self.toggle_btn = tk.Button(
            self.root, 
            text="Toggle Dark Mode", 
            command=self.toggle_theme,
            font=("Arial", 10),
            padx=10,
            pady=5
        )
        self.toggle_btn.pack(side=tk.BOTTOM, pady=20)

        # Status Label
        self.status_label = tk.Label(self.root, text="Current Theme: Light Mode", font=("Arial", 8))
        self.status_label.pack(side=tk.BOTTOM)

    def toggle_theme(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
        else:
            self.current_theme = "light"
        
        self.apply_theme()

    def apply_theme(self):
        theme = self.themes[self.current_theme]
        
        # Root window
        self.root.config(bg=theme["bg"])

        # Update labels (widgets that support fg)
        labels_to_update = [
            (self.header_label, theme["bg"], theme["accent"]),
            (self.moto_name, theme["card_bg"], theme["accent"]),
            (self.moto_desc, theme["card_bg"], theme["fg"]),
            (self.status_label, theme["bg"], theme["fg"])
        ]

        for widget, bg, fg in labels_to_update:
            widget.config(bg=bg, fg=fg)

        # Update frames (only bg)
        self.card_frame.config(bg=theme["card_bg"])

        # Special handling for buttons
        self.rent_btn.config(bg=theme["accent"], fg="#000000", borderwidth=0)
        self.toggle_btn.config(bg=theme["btn_bg"], fg=theme["btn_fg"])

        # Update status text
        mode_text = self.current_theme.capitalize()
        self.status_label.config(text=f"Current Theme: {mode_text} Mode")
        
        print(f"Theme changed to: {self.current_theme}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MotoRentalApp(root)
    root.mainloop()

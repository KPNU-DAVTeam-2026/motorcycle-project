import unittest
import tkinter as tk
from src.dark_mode_gui import MotoRentalApp
іогапоцщшпшщоцущшкуопщшівуп
class TestDarkMode(unittest.TestCase):
    def setUp(self)
        self.root = tk.Tk()
        # Withdraw the window so it doesn't actually pop up during tests
        self.root.withdraw()
        self.app = MotoRentalApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initial_theme(self):
        self.assertEqual(self.app.current_theme, "light")

    def test_toggle_theme(self):
        self.app.toggle_theme()
        self.assertEqual(self.app.current_theme, "dark")
        self.app.toggle_theme()
        self.assertEqual(self.app.current_theme, "light")

    def test_theme_colors_exist(self):
        self.assertIn("light", self.app.themes)
        self.assertIn("dark", self.app.themes)
        for theme in self.app.themes.values():
            self.assertIn("bg", theme)
            self.assertIn("fg", theme)
            self.assertIn("accent", theme)

if __name__ == "__main__":
    unittest.main()

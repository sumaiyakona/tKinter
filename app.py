# app.py
import tkinter as tk
from app_interface import App

# Function to run the GUI
def run_gui():
    root = tk.Tk()  # Create root window
    app = App(master=root)
    app.mainloop()  # Start Tkinter event loop

if __name__ == "__main__":
    run_gui()
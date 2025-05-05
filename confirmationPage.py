# Author : Rutuja Rashmi
# Date : 05/02/25

import tkinter as tk
from PIL import Image, ImageTk

# Class to display the confirmation window
class ConfirmationWindow:
    def __init__(self, master, name, size):
        self.window = tk.Toplevel(master)
        self.window.title("Pizza Station!! Order Confirmation")
        self.window.geometry("400x400")

        # Displaying the message
        msg = f"Thank you, {name}!\n\nYour {size} pizza is on the way!"
        tk.Label(self.window, text=msg, font=("Helvetica", 12)).pack(pady=15)

        self.image2 = Image.open("images/pizza2.png")
        self.photo2 = ImageTk.PhotoImage(self.image2)
        img_label = tk.Label(self.window, image=self.photo2, text="Enjoy your Pizza", compound=tk.BOTTOM)
        img_label.image = self.photo2
        img_label.pack()

        # Back button to go back to the main screen
        tk.Button(self.window, text="Back to Main", command=self.go_back).pack(pady=10)

    def go_back(self): #action for the back button
        self.window.destroy()
        self.window.master.deiconify()



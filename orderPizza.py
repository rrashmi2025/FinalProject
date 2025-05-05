# Author : Rutuja Rashmi
# Date : 05/02/25

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from confirmationPage import ConfirmationWindow

# Class for Pizza Ordering
class OrderPizza:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Station")
        self.root.geometry("400x500")

        # Labels to show on the GUI for the Users
        tk.Label(root, text="Welcome to Pizza Station!").pack(pady=10)
        tk.Label(root, text="Enter your name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack(pady=5)

        tk.Label(root, text="Select pizza size:").pack()
        self.size_var = tk.StringVar()
        self.size_var.set("Medium")  # A default value for the users

        sizes = ["Small", "Medium", "Large"]
        for size in sizes:
            tk.Radiobutton(root, text=size, variable=self.size_var, value=size).pack()

        # import images for the GUI to display
        self.image1 = Image.open("images/pizza1.png")
        self.photo1 = ImageTk.PhotoImage(self.image1)
        img_label = tk.Label(root, image=self.photo1, text="Order your Pizza", compound=tk.BOTTOM)
        img_label.image = self.photo1
        img_label.pack(pady=10)

        # Define the buttons and the actions
        tk.Button(root, text="Place Order", command=self.place_order).pack(pady=5)
        tk.Button(root, text="Clear", command=self.clear_inputs).pack(pady=5)
        tk.Button(root, text="Exit", command=self.exit_app).pack(pady=5)

    def validate_inputs(self): # validating the input for the names
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Input Error", "Name is required.")
            return None
        if not name.replace(" ", "").isalpha():
            messagebox.showerror("Input Error", "Please enter a valid name.")
            return None
        return name

    def place_order(self): # Taking the inputs and calling the 2nd window for confirmation
        name = self.validate_inputs()
        if name:
            size = self.size_var.get()
            self.root.withdraw()
            ConfirmationWindow(self.root, name, size)

    def clear_inputs(self): # This action will clear the form 
        self.name_entry.delete(0, tk.END)
        self.size_var.set("Medium")

    def exit_app(self): # This action will exit the application
        if messagebox.askokcancel("Exit", "Exit the PizzaStation App?"):
            self.root.destroy()

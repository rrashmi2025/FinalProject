# Author : Rutuja Rashmi
# Date : 05/02/25

from tkinter import Tk
from orderPizza import OrderPizza

def main():
    root = Tk()
    app = OrderPizza(root)
    root.mainloop()

if __name__ == "__main__":
    main()

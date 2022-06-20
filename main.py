import sys

import search as sh
import tkinter as tk

# GUI

# main scene
# window = tk.Tk()
# window.geometry("500x600")
# window.title("Stock Analyzer")
#
# # component
# message = tk.Label(
#     text="Enter Symbol",
#     font=("Helvetica", 15, "bold"),
#     height="3",
# )
# message.pack()
# tk.Entry(bd="10px", font="10px").pack()
# window.mainloop()

# initialize variables
repeat = 'Y'
while repeat == 'Y':
    # Welcome Message
    print("Hi, please type the symbol you are searching for.\n")
    # User Input
    symbol = input("Enter symbol: ").upper()
    # Important Message
    print("\n\t\t\t\t\tHere are the details for " + symbol)
    print("--------------------------------------------------------------------")
    try:
        target = sh.Symbol(symbol)
    except TypeError:
        sys.exit("Symbol not found")
    repeat = input("Y / N ").upper()

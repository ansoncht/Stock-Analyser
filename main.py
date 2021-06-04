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

# initialize variable
repeat = 'Y'
while repeat == 'Y':
    # Welcome Message
    print("Hi, please type the symbol you are searching for.\n")
    # User Input
    symbol = input("Enter symbol: ").upper()
    # Important Message
    print("\n\t\t\t\t\tHere are the details for " + symbol)
    print("--------------------------------------------------------------------")
    target = sh.Symbol(symbol)
    repeat = input("Y / N ").upper()

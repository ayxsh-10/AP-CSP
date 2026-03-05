#imports
import tkinter as tk
from tkinter import messagebox

#list of data inputs
expenses = []

#event handlers
def add_expense():
    name = name_entry.get()
    amount = amount_entry.get()

    #input validation
    if name == "":
        messagebox.showerror("Input Error", "The expense must have a name.")
        return

    try:
        amount = float(amount)
        if amount < 0:
            messagebox.showerror("Input Error", "The amount must be positive.")
            return
    except ValueError:
        messagebox.showerror("Input Error", "The amount must be a number.")
        return

    #program logic
    expenses.append((name, amount))
    expense_list.insert(tk.END, name + ": $" + str(round(amount, 2)))

    #clear input boxes
    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

#take sum of all totals
def calculate_total():
    total = sum(amount for _, amount in expenses)
    total_label.config(text=f"Total Expenses: " + str(round(total, 2)))

#clear expense list
def clear_expenses():
    expenses.clear()
    expense_list.delete(0, tk.END)
    total_label.config(text="Total Expenses: $0.00")


#GUI Design

window = tk.Tk()
window.title("Expense Tracker")
window.geometry("450x500")

#title
tk.Label(window, text="Expense Tracker", font=("Arial", 16)).pack(pady=10)

#expense name textbox
tk.Label(window, text="Expense Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

#amount input
tk.Label(window, text="Amount ($)").pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

#submit expense to list
add_button = tk.Button(window, text="Add Expense", command=add_expense)
add_button.pack(pady=5)

#display list
expense_list = tk.Listbox(window, width=40)
expense_list.pack(pady=10)

#compute the total of the expenses
total_button = tk.Button(window, text="Calculate Total", command=calculate_total)
total_button.pack(pady=5)

#clear list
clear_button = tk.Button(window, text="Clear All", command=clear_expenses)
clear_button.pack(pady=5)

#total expenses list
total_label = tk.Label(window, text="Total Expenses: $0.00", font=("Arial", 12))
total_label.pack(pady=10)

#program code initialization
window.mainloop()


""""
Program Explanation

This program tracks expenses that are entered by the user,
and then allows the user to input an expense name and amount.
From there, it displays the expenses in a list,
and calculates the total spending.

The user types an expense name and amount into the text boxes 
and clicks the Add Expense button, to make them appear in a list.
The user clicks "Calculate Total" to see the total cost
or "Clear All" to reset the list.

User input is handled in the add_expense() function
using name_entry.get() and amount_entry.get().

Programming logic is implemented in add_expense()
where expenses are stored and validated, and in
calculate_total() where the total expense amount is calculated.

"""
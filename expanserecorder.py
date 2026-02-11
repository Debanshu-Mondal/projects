import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from datetime import datetime
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x600")
expenses = []
def addexp():
    date = entry_date.get()
    desc = entry_desc.get()
    ctg = entry_ctg.get()
    amt = entry_amt.get()
    if not (date and desc and ctg and amt):
        messagebox.showwarning("Input Error", "All the boxes must be filled!")
        return
    try:
        float(amt)  # allow decimal numbers too
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number!")
        return
    detail = [date, desc, ctg, amt]
    expenses.append(detail)
    tree.insert('', 'end', values=detail)
    entry_date.delete(0, tk.END)
    entry_desc.delete(0, tk.END)
    entry_ctg.delete(0, tk.END)
    entry_amt.delete(0, tk.END)
def createcsv():
    if not expenses:
        messagebox.showinfo("No Data!", "Enter the data")
        return
    filepath = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")]
    )
    if not filepath:
        return
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Description", "Category", "Amount"])
        writer.writerows(expenses)
    messagebox.showinfo("Success", f"Records exported to:\n{filepath}")
dis = tk.Frame(root)
dis.pack(pady=10)
tk.Label(dis, text="Date").grid(row=0, column=0)
tk.Label(dis, text="Description").grid(row=1, column=0)
tk.Label(dis, text="Category").grid(row=2, column=0)
tk.Label(dis, text="Amount").grid(row=3, column=0)
entry_date = tk.Entry(dis)
entry_desc = tk.Entry(dis)
entry_ctg = tk.Entry(dis)
entry_amt = tk.Entry(dis)
entry_date.grid(row=0, column=1)
entry_desc.grid(row=1, column=1)
entry_ctg.grid(row=2, column=1)
entry_amt.grid(row=3, column=1)
tk.Button(dis, text="ADD EXPENSE", command=addexp).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(dis, text="Export to .csv file", command=createcsv).grid(row=5, column=0, columnspan=2)
columns = ("Date", "Description", "Category", "Amount")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER)
tree.pack(fill='both', expand=True, pady=10)
root.mainloop()

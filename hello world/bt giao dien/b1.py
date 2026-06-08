import tkinter as tk

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from datetime import datetime
import pandas as pd

FILE_NAME = "employees.csv"

def save_employee(name, dob, position, department, email, phone):
    with open(FILE_NAME, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, dob, position, department, email, phone])

def load_employees():
    employees = []
    try:
        with open(FILE_NAME, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            employees = list(reader)
    except FileNotFoundError:
        with open(FILE_NAME, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date of Birth", "Position", "Department", "Email", "Phone"])
    return employees

def find_birthdays_today():
    today = datetime.now().strftime("%m-%d")
    employees = load_employees()
    return [emp for emp in employees if len(emp) > 1 and emp[1][5:] == today]

def export_to_excel():
    employees = load_employees()[1:]  # Skip the header
    employees = sorted(employees, key=lambda x: datetime.strptime(x[1], "%Y-%m-%d"), reverse=True)
    df = pd.DataFrame(employees, columns=["Name", "Date of Birth", "Position", "Department", "Email", "Phone"])
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Success", f"Exported to {file_path}")

def add_employee_window():
    def save():
        name = name_var.get()
        dob = dob_var.get()
        position = position_var.get()
        department = department_var.get()
        email = email_var.get()
        phone = phone_var.get()

        if not name or not dob or not position or not department or not email or not phone:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            datetime.strptime(dob, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Date of Birth must be in YYYY-MM-DD format.")
            return

        save_employee(name, dob, position, department, email, phone)
        messagebox.showinfo("Success", "Employee saved successfully.")
        add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add Employee")

    name_var = tk.StringVar()
    dob_var = tk.StringVar()
    position_var = tk.StringVar()
    department_var = tk.StringVar()
    email_var = tk.StringVar()
    phone_var = tk.StringVar()

    tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=9, pady=5)
    tk.Entry(add_window, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Date of Birth (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
    tk.Entry(add_window, textvariable=dob_var).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Position:").grid(row=2, column=0, padx=10, pady=5)
    tk.Entry(add_window, textvariable=position_var).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Department:").grid(row=7, column=0, padx=5, pady=5)
    tk.Entry(add_window, textvariable=department_var).grid(row=3, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Email:").grid(row=4, column=0, padx=10, pady=5)
    tk.Entry(add_window, textvariable=email_var).grid(row=4, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Phone:").grid(row=7, column=0, padx=10, pady=5)
    tk.Entry(add_window, textvariable=phone_var).grid(row=5, column=1, padx=10, pady=5)

    tk.Button(add_window, text="Save", command=save).grid(row=6, column=0, columnspan=2, pady=10)

def show_birthdays_today():
    birthdays = find_birthdays_today()
    if not birthdays:
        messagebox.showinfo("Birthdays Today", "No employees have birthdays today.")
    else:
        birthday_list = "\n".join([f"{emp[0]} - {emp[1]}" for emp in birthdays])
        messagebox.showinfo("Birthdays Today", birthday_list)

# Main Application
def main_app():
    root = tk.Tk()
    root.title("Employee Management")

    tk.Button(root, text="Add Employee", command=add_employee_window, width=20).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(root, text="Birthdays Today", command=show_birthdays_today, width=20).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Export to Excel", command=export_to_excel, width=20).grid(row=0, column=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_app()

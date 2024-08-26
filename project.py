import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def main():
    create_gui()

def create_gui():
    root = tk.Tk()
    root.title("Calculate Days Until Birthday")
    root.configure(bg='#a3b18a') 
    window_width = 400
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")
    
    birthday_label = tk.Label(root, text="Enter your birthday (DD/MM):", bg='#a3b18a')
    birthday_label.pack(pady=20)

    global birthday_entry
    birthday_entry = tk.Entry(root)
    birthday_entry.pack(pady=5)

    calculate_button = tk.Button(root, text="Calculate", command=calculate_days_until_birthday_from_input)
    calculate_button.pack(pady=30)

    root.mainloop()

def calculate_days_until_birthday_from_input():
    birthday_str = birthday_entry.get()
    message = get_message_based_on_input(birthday_str)
    if "Please enter a valid date" in message:
        messagebox.showerror("Error", message)
    else:
        messagebox.showinfo("Days Until Birthday", message)

def get_message_based_on_input(birthday_str):
    if is_valid_date(birthday_str):
        days_until = calculate_days_until_birthday(birthday_str)
        return f"There are {days_until} days until your birthday!"
    else:
        return "Please enter a valid date in the format DD/MM."
    
def calculate_days_until_birthday(birthday_str):
    birthday = datetime.strptime(birthday_str, "%d/%m")
    today = datetime.today()

    current_year_birthday = birthday.replace(year=today.year)

    if current_year_birthday < today:
        next_birthday = current_year_birthday.replace(year=today.year + 1)
    else:
        next_birthday = current_year_birthday

    return (next_birthday - today).days

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
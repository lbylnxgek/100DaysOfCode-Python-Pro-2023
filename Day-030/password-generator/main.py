from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project, modified to use list comprehension, .join and
    # not need user input

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("./data.json", mode="r") as data_file:
            # Read existing data from file as dictionary
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(
            title="Error!",
            message="No data file found, please save at least one record.",
        )
    else:
        if website in data:
            account = data[website]["account"]
            password = data[website]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(
                title=f"{website}",
                message=f"Email: {account}\nPassword: {password}\n\nPassword copied to clipboard.",
            )
        else:
            messagebox.showinfo(
                title=f"{website}", message="No details for the website exist."
            )


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    account = account_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "account": account,
            "password": password,
        }
    }

    if len(website) == 0 or len(account) == 0 or len(password) == 0:
        messagebox.showerror(
            title="D'oh!", message="Please don't leave any fields empty"
        )
    else:
        # Open existing data file, if one exists
        try:
            with open("./data.json", mode="r") as data_file:
                # Read existing data from file as dictionary
                data = json.load(data_file)

        # No existing data file, create one
        except FileNotFoundError:
            with open("./data.json", mode="w") as data_file:
                # Write data to file as JSON
                json.dump(new_data, data_file, indent=4)

        else:
            # Add new entry to dictionary
            data.update(new_data)

            # Write data to file as JSON
            with open("./data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            account_entry.delete(0, END)
            account_entry.insert(0, string="bob@loblaw.com")
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

account_label = Label(text="Email/Username:")
account_label.grid(row=2, column=0)

account_entry = Entry(width=50)
account_entry.grid(row=2, column=1, columnspan=2)
account_entry.insert(0, string="bob@loblaw.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_record_button = Button(text="Add", width=44, command=save)
add_record_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    account = account_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(account) == 0 or len(password) == 0:
        messagebox.showerror(
            title="D'oh!", message="Please don't leave any fields empty"
        )
    else:
        entry_ok = messagebox.askokcancel(
            title=website,
            message=f"You entered:\nEmail: {account}\nPassword: {password}\nOk to save?",
        )
        if entry_ok:
            with open(f"./data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {account} | {password}\n")

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

website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

account_label = Label(text="Email/Username:")
account_label.grid(row=2, column=0)

account_entry = Entry(width=50)
account_entry.grid(row=2, column=1, columnspan=2)
account_entry.insert(0, string="bob@loblaw.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_record_button = Button(text="Add", width=42, command=save)
add_record_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

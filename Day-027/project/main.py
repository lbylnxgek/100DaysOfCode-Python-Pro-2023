from tkinter import *


# Button action
def miles_to_km():
    miles = float(miles_input.get())
    kilometers = round(miles * 1.609, 2)
    km.config(text=f"{kilometers}")


# Create window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=25, pady=25)

# Entry for miles
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Equal to label
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

# Km
km = Label(text="0")
km.grid(column=1, row=1)

# Km label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()

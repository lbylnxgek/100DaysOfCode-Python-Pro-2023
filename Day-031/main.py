from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/french_words.csv")
words_to_learn = data.to_dict(orient="records")


# ---------------------------  CREATE CARD ----------------------------- #
def create_card():
    random_word = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text=f"French")
    canvas.itemconfig(card_word, text=f"{random_word["French"]}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Me! - French to English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=create_card)
unknown_button.grid(row=1, column=0)

known_image = PhotoImage(file="./images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=create_card)
known_button.grid(row=1, column=1)

create_card()

window.mainloop()

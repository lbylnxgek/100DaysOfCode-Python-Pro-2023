from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

words_to_learn = data.to_dict(orient="records")
current_word = {}


def create_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words_to_learn)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")


def word_is_known():
    words_to_learn.remove(current_word)
    print(len(words_to_learn))
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)

    create_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Me! - French to English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=create_card)
unknown_button.grid(row=1, column=0)

known_image = PhotoImage(file="./images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=word_is_known)
known_button.grid(row=1, column=1)

create_card()

window.mainloop()

import cipher_letters
import art
alphabet = cipher_letters.alphabet
logo = art.logo

def caesar(input_text, shift_number, cipher_direction):
    output_text = ""

    for letter in input_text:
        if letter not in alphabet:
            output_text += letter
        else:
            position = alphabet.index(letter)
            if cipher_direction == "encode":
                output_letter = alphabet[position + shift_number]
            else:
                output_letter = alphabet[position - shift_number]
            output_text += output_letter

    print(f"The {direction}d text is: {output_text}\n")

print(logo)

go_again = "y"
while go_again == "y":
    direction = "none"
    while direction != "encode" and direction != "decode":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

    text = input("Type your message: ").lower()

    shift = 0
    while shift < 1 or shift > 25:
        shift = int(input("Type the shift number (1-25): "))

    caesar(input_text=text, shift_number=shift, cipher_direction=direction)
    go_again = input("Type 'y' if you want to go again: ").lower()

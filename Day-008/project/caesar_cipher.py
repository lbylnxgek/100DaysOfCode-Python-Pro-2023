import cipher_letters
import art

alphabet = cipher_letters.alphabet
logo = art.logo


def caesar(input_text, shift_number, cipher_direction):
    output_text = ""

    # Process each char in the input_text
    for char in input_text:
        # If char is not a letter, just add it to the output_text
        if char not in alphabet:
            output_text += char
        # char is a letter
        else:
            # Determine index in alphabet list
            position = alphabet.index(char)
            # encode chosen, use position + shift_number for cipher letter
            if cipher_direction == "encode":
                output_char = alphabet[position + shift_number]
            # decode chosen, use position - shift_number for plain letter
            else:
                output_char = alphabet[position - shift_number]
            # Add char to output_text
            output_text += output_char

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

print("\nGoodbye!")

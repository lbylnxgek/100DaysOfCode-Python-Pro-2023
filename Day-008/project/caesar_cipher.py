import cipher_letters
alphabet = cipher_letters.alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(input_text, shift_number, cipher_direction):
    output_text = ""

    for letter in input_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            output_letter = alphabet[position + shift_number]
        else:
            output_letter = alphabet[position - shift_number]
        output_text += output_letter

    print(f"The {direction}d text is: {output_text}")

caesar(input_text=text, shift_number=shift, cipher_direction=direction)

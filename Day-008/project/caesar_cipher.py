import cipher_letters
alphabet = cipher_letters.alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_number):
    cipher_text = ""

    for plain_letter in plain_text:
        position = alphabet.index(plain_letter)
        cipher_letter = alphabet[position + shift_number]
        # DEBUG:
        #print(f"{plain_letter} -> {cipher_letter}")
        cipher_text += cipher_letter
    
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_number):
    plain_text = ""

    for cipher_letter in cipher_text:
        position = alphabet.index(cipher_letter) + 26
        plain_letter = alphabet[position - shift_number]
        # DEBUG:
        #print(f"{cipher_letter} -> {plain_letter}")
        plain_text += plain_letter

    print(f"The decoded text is {plain_text}")

if direction == "encode":
    encrypt(plain_text=text, shift_number=shift)
else:
    decrypt(cipher_text=text, shift_number=shift)

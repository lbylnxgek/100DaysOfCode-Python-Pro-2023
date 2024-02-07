NAME_PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    stripped_name = name.strip()
    new_letter = starting_letter.replace("Angela", "Zane")
    new_letter = new_letter.replace(NAME_PLACEHOLDER, stripped_name)
    with open(
        f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w"
    ) as output_file:
        output_file.write(f"{new_letter}")

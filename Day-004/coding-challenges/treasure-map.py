# Initialize variables
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

# Print greeting & capture input
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

# Convert column to lowercase
input_column = position[0].lower()
input_row = position[1]

# Set value of output_column
if input_column == "a":
  output_column = 0
elif input_column == "b":
  output_column = 1
else:
  output_column = 2

# Write X to correct line (row) based on input_row
if input_row == "1":
  line1[output_column] = "X"
elif input_row == "2":
  line2[output_column] = "X"
else:
  line3[output_column] = "X"

print(f"{line1}\n{line2}\n{line3}")

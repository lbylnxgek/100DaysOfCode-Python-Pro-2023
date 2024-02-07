# Method #1, remember to close when finished
file = open("data.txt")
contents = file.read()
print(contents)
file.close()

# Method #2, let with handle closing the file
with open("data.txt") as file:
    contents = file.read()

# Open file in append mode
with open("data.txt", mode="a") as file:
    file.write("\nBlah, blah, something, something, ham sandwich")

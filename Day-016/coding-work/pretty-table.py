from prettytable import PrettyTable

table = PrettyTable()

print(table.align)
table.align = "r"
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

print(table)

import pandas

# Read CSV data file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get numpy.ndarray of unique colors from data, excluding blanks
# This avoids needing to know the colors ahead of time
fur_colors = data["Primary Fur Color"].dropna().unique()
fur_colors.sort()

# Create colors and count lists
fur_colors_list = []
fur_colors_count_list = []
for color in fur_colors:
    fur_colors_list.append(color)
    count = len(data[data["Primary Fur Color"] == color])
    fur_colors_count_list.append(count)

# Create dictionary from lists
data_dict = {}
data_dict["Fur Color"] = fur_colors_list
data_dict["Count"] = fur_colors_count_list

# Create dataframe from dictionary
df = pandas.DataFrame(data_dict)
print(df)

# Output to CSV file
df.to_csv("squirrel_color_count.csv")

# NOTE for later - or not, as the case may be.  Tired of fighting with it for now:
# This produces a nice dataframe (below), but I was unable to remove the
# "table label", rename the "Primary Fur Color" column label to "fur color"
# or add a label to the count column.
# What I like about this potential solution is I don't have to know all of the
# fur colors ahead of time.
# fur_data = pandas.DataFrame(
#     data.groupby(["Primary Fur Color"])["Primary Fur Color"].count()
# )
# This relabels the "table label", not the column label:
# fur_data.rename(columns={"Primary Fur Color": "fur color"}, inplace=True)
# print(fur_data)
#                    fur color
# Primary Fur Color
# Black                    103
# Cinnamon                 392
# Gray                    2473
# Purple                     1

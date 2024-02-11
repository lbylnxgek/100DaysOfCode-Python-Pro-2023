import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

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

# This produces a list of colors excluding blanks, which *in theory* should
# be useful in a for loop to grab counts, again without having to know all
# of the fur colors ahead of time.  I may be able to use this one with
# her solution, we'll see.  type() reports numpy.ndarray, which I am not
# currently familiar with.
# fur_colors = data["Primary Fur Color"].dropna().unique()
# fur_colors.sort()

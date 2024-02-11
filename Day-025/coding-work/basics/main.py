# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# temp_avg = sum(temp_list) / len(temp_list)
# print(temp_avg)

# print(data["temp"].mean())
# print(data["temp"].max())

# # Get data in columns
# # Like dictionary key
# print(data["condition"])
# # Like object attribute
# print(data.condition)

# Get data in column
#print(data[data.day == "Monday"])

# Get row with max temp
#print(data[data.temp == data.temp.max()])

# Convert Monday's temperature to Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp_c = monday.temp[0]
# monday_temp_f = (monday_temp_c * 9/5) + 32
# print(monday_temp_c)
# print(monday_temp_f)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

# Write to CSV file
data.to_csv("student_data.csv")

# Write to Excel file
data.to_excel("student_data.xlsx")
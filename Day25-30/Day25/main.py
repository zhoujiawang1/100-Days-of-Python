import pandas
import csv

path = "Day25-/Day25/weather_data.csv"
path2 = "Day25-/Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

data = pandas.read_csv(path2)
print(data.groupby("Primary Fur Color").size())
new_data = data.groupby("Primary Fur Color").size()
print(type(new_data))
new_data.to_csv("Day25-/Day25/squirrel.csv")
# lines = file.readlines()

# data = []
# # for line in lines:
# #     data.append(line)
# # print(data)

# # data = csv.reader(file)
# # temp = []
# # for row in data:
# #     print(row)

# data = pandas.read_csv(path)
# # print(data['temp'])
# # print(type(data))  # data frame = table
# # # theres another type
# # print(data['temp'])  # equivalent of a list, like the column

# # data_dict = data.to_dict()
# # print(data_dict)

# # temp_list = data['temp'].to_list()
# # print(temp_list)
# # avg = data['temp'].mean()
# # print(avg)

# # maximum value
# print(data['temp'].max())
# print(data.temp.max())

# # get data in row
# print(data[data.temp == data.temp.max()])

# # create dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# new_data.to_csv("Day25-/Day25/new_data.csv")

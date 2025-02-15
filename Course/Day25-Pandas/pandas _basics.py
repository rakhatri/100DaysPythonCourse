# # with open("weather_data.csv") as weather_data:
# #     lines = weather_data.readlines()
# #     print(lines)
#
# # import csv
# #
# # with open("weather_data.csv") as weather_data:
# #     data = csv.reader(weather_data)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #
# # print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # temp_list = data["temp"].to_list()
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print((monday.temp[0] * 9/5) + 32)
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250214.csv")

color_data = data.groupby("Primary Fur Color").size().reset_index(name="Count")
print(color_data)

color_data.to_csv("output.csv")
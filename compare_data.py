from matplotlib import pyplot as plt
from matplotlib import rc

import pandas as pd
import numpy as np

directory = "./Data/TAAS/"

df_all_data = pd.read_csv(directory + "all_data.csv", encoding="UTF-8")
df_all_data.drop(columns=["Unnamed: 0"], inplace=True)

df_all_data_condition = pd.read_csv(directory + "after_merge_damage_violent/" + "all_data_condition.csv", encoding="UTF-8")
df_all_data_condition.drop(columns=["Unnamed: 0", "Unnamed: 0.1"], inplace=True)

print(df_all_data.shape)
print(df_all_data_condition.shape)
print("----------")

# Count the number of rows that have the same value in the column "시군구"
location_list_all = {}
location_list_condition = {}

for location in df_all_data_condition["시군구"]:
  if location not in location_list_condition:
    location_list_condition[location] = 1
  else:
    location_list_condition[location] += 1

for location in df_all_data["시군구"]:
  if location not in location_list_all:
    location_list_all[location] = 1
  else:
    location_list_all[location] += 1

location_list_condition_SORTED = dict(sorted(location_list_condition.items(), key=lambda item: item[1], reverse=True))
location_list_all_SORTED = dict(sorted(location_list_all.items(), key=lambda item: item[1], reverse=True))

data_dict = {}

for location in location_list_condition_SORTED:
  if location in location_list_all_SORTED:
    # print("[ " + location + "] 의 전체 사상자 수 : " + str(location_list_all_SORTED[location]) + ", 조건부 사상자 수 : " + str(location_list_condition_SORTED[location]))
    data_dict[location] = [location_list_all_SORTED[location], location_list_condition_SORTED[location]]

location_seoul = [location for location in data_dict.keys()]
values = [value for value in data_dict.values()]
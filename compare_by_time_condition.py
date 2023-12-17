from matplotlib import pyplot as plt
from matplotlib import rc

import pandas as pd

dircetory = "./Data/TAAS/"

df_all_data_condition = pd.read_csv(dircetory + "after_merge_damage_violent/" + "all_data_condition.csv", encoding="UTF-8")
df_all_data_condition.drop(columns=["Unnamed: 0", "Unnamed: 0.1"], inplace=True)

data_by_time_condition = {}

for time in range(2007, 2023, 1):
  if time not in data_by_time_condition.keys():
    data_by_time_condition[time] = 0

for accident_num in df_all_data_condition["사고번호"]:
  if accident_num // 1000000000000 in data_by_time_condition.keys():
    data_by_time_condition[accident_num // 1000000000000] += 1

# Check the number of accidents by time and Compare with original dataframes
# count = 0

# for time in data_by_time_condition.values():
#   count += time

# print(count)
# print(df_all_data_condition.shape)

rc('font', family='AppleGothic')
plt.plot([time for time in data_by_time_condition.keys()], [time for time in data_by_time_condition.values()], color="red")
plt.xticks([time for time in data_by_time_condition.keys()])
plt.show()
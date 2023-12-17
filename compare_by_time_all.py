from compare_by_time_condition import data_by_time_condition

from matplotlib import pyplot as plt
from matplotlib import rc

import pandas as pd

dircetory = "./Data/TAAS/"

df_all_data = pd.read_csv(dircetory + "all_data.csv", encoding="UTF-8")

data_by_time_all = {}

for time in range(2007, 2023, 1):
  if time not in data_by_time_all.keys():
    data_by_time_all[time] = 0

for accident_num in df_all_data["사고번호"]:
  if accident_num // 1000000000000 in data_by_time_all.keys():
    data_by_time_all[accident_num // 1000000000000] += 1

rc('font', family='AppleGothic')
plt.plot([time for time in data_by_time_all.keys()], [time for time in data_by_time_all.values()], color="red", label="전체 사고 수")
plt.plot([time for time in data_by_time_condition.keys()], [time for time in data_by_time_condition.values()], color="blue", label="조건부 사고 수")
plt.scatter([time for time in data_by_time_all.keys()], [time for time in data_by_time_all.values()], color="red")
plt.scatter([time for time in data_by_time_condition.keys()], [time for time in data_by_time_condition.values()], color="blue")
plt.xticks([time for time in data_by_time_all.keys()])
plt.grid(True)
plt.show()
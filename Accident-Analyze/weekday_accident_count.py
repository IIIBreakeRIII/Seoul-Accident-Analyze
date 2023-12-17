from gm_data import get_data as gd

import pandas as pd
import matplotlib.pyplot as plt

condition_data_monday = pd.DataFrame(gd("SELECT weekday FROM taas_condition_data WHERE weekday='월요일';"))
condition_data_tuesday = pd.DataFrame(gd("SELECT weekday FROM taas_condition_data WHERE weekday='화요일';"))
condition_data_wendesday = pd.DataFrame(gd("SELECT weekday FROM taas_condition_data WHERE weekday='수요일';"))
condition_data_thursday = pd.DataFrame(gd("SELECT weekday FROM taas_condition_data WHERE weekday='목요일';"))
condition_data_friday = pd.DataFrame(gd("SELECT weekday FROM taas_condition_data WHERE weekday='금요일';"))
condition_data_saturday = pd.DataFrame(gd("SELECT weekday FROM taas_condition_data WHERE weekday='토요일';"))
condition_data_sunday = pd.DataFrame(gd("SELECT weekday FROM taas_condition_data WHERE weekday='일요일';"))

condition_data_counts = pd.DataFrame(gd("SELECT weekday, COUNT(*) as count FROM taas.taas_condition_data GROUP BY weekday"),columns = ['weekday', 'count'])
all_data_counts = pd.DataFrame(gd("SELECT weekday, COUNT(*) as count FROM taas.taas_all_data GROUP BY weekday"),columns = ['weekday', 'count'])

print(condition_data_monday.shape)
print(condition_data_tuesday.shape)
print(condition_data_wendesday.shape)
print(condition_data_thursday.shape)
print(condition_data_friday.shape)
print(condition_data_saturday.shape)
print(condition_data_sunday.shape)


plt.plot(condition_data_counts['weekday'], condition_data_counts['count'])
plt.plot(all_data_counts['weekday'], all_data_counts['count'])

plt.xlabel('요일')
plt.ylabel('사고건수')
# plt.figure(figsize=(15,6))
plt.title('요일별 사상자수')
plt.grid(True)
# plt.grid(True)
# plt.tight_layout()
plt.show()


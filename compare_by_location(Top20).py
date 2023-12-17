from compare_data import location_seoul, values

from matplotlib import pyplot as plt
from matplotlib import rc

# location_seoul = location_seoul[:20]
# values = values[:20]

rc('font', family='AppleGothic')
# plt.plot(location_seoul, [value[0] for value in values], color="red", label="전체 사상자 수")
# plt.plot(location_seoul, [value[1] for value in values], color="blue", label="조건부 사상자 수")
plt.plot(location_seoul, [value[0] for value in values], color="orange", label="전체 사상자 수")
plt.plot(location_seoul, [value[1] for value in values], color="green", label="조건부 사상자 수")
plt.xticks(rotation=90)
plt.legend()
plt.show()
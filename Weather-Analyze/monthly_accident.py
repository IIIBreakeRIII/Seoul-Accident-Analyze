from data_from_server import get_data as gd

import matplotlib.pyplot as plt
import pandas as pd

all_month_query = """
SELECT
  SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', 2), ' ', -1) AS accident_month,
  COUNT(*) AS count_per_month
FROM
	taas_all_data
GROUP BY
  accident_month
ORDER BY
  accident_month;
"""

condition_month_query = """
SELECT
  SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', 2), ' ', -1) AS accident_month,
  COUNT(*) AS count_per_month
FROM
	taas_condition_data
GROUP BY
  accident_month
ORDER BY
  accident_month;
"""

df_all_month = pd.DataFrame(gd(all_month_query), columns=['accident_month', 'count_per_month'])
df_condition_month = pd.DataFrame(gd(condition_month_query), columns=['accident_month', 'count_per_month'])

all_month_dict = dict(zip(df_all_month['accident_month'], df_all_month['count_per_month']))
condition_month_dict = dict(zip(df_condition_month['accident_month'], df_condition_month['count_per_month']))

data = all_month_dict.pop('10월')
all_month_dict['10월'] = data

data = all_month_dict.pop('11월')
all_month_dict['11월'] = data

data = all_month_dict.pop('12월')
all_month_dict['12월'] = data

data = condition_month_dict.pop('10월')
condition_month_dict['10월'] = data

data = condition_month_dict.pop('11월')
condition_month_dict['11월'] = data

data = condition_month_dict.pop('12월')
condition_month_dict['12월'] = data

# Convert dictionaries to pandas Series
all_month_series = pd.Series(all_month_dict)
condition_month_series = pd.Series(condition_month_dict)

weather_average_query = """
SELECT
    DATE_FORMAT(STR_TO_DATE(date, '%Y-%m-%d %H:%i'), '%m') AS 월,
    ROUND(AVG(CAST(temp AS DECIMAL(5, 1))), 1) AS 월평균온도
FROM
    weather_new
WHERE
    STR_TO_DATE(date, '%Y-%m-%d %H:%i') BETWEEN '2007-01-01 00:00' AND '2022-12-31 23:59'
GROUP BY
    월
ORDER BY
    월;
"""

df_weather_average = pd.DataFrame(gd(weather_average_query), columns=['월', '월평균온도'])

plt.figure()
# plt.bar(all_month_series.index, all_month_series.values, label='All Month')
plt.plot(all_month_series.index, all_month_series.values, label='All Month')
plt.xlabel('Month')
plt.ylabel('Accident Count')
plt.title('Accident Count per Month - All')
plt.xticks(range(1, 13))

plt.figure()
# plt.bar(condition_month_series.index, condition_month_series.values, label='Condition Month')
plt.plot(condition_month_series.index, condition_month_series.values, label='Condition Month')
plt.xlabel('Month')
plt.ylabel('Accident Count')
plt.title('Accident Count per Month - Condition')
plt.xticks(range(1, 13))

plt.figure()
# plt.bar(df_weather_average['월'], df_weather_average['월평균온도'], label='Average Temperature')
plt.plot(df_weather_average['월'], df_weather_average['월평균온도'], marker='o', color='green', linestyle='-')
plt.xlabel('Month')
plt.ylabel('Average Temperature')
plt.title('Average Temperature per Month')
plt.xticks(range(1, 13))
plt.show()
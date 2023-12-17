from data_from_server import get_data as gd

import matplotlib.pyplot as plt
import pandas as pd

humidity_query = """
SELECT
    humidity_ranges.low AS humidity_range_low,
    humidity_ranges.high AS humidity_range_high,
    COUNT(*) AS days_count
FROM (
    SELECT
        DATE(`date`) AS day,
        ROUND(AVG(CAST(`humidity` AS DECIMAL(5,2))), 2) AS avg_humidity
    FROM
        weather_new
    WHERE
        `date` BETWEEN '2007-01-01 00:00' AND '2022-12-31 23:59'
    GROUP BY
        day
    HAVING
        avg_humidity >= 0
) AS weather_dates
CROSS JOIN (
    SELECT 0 AS low, 10 AS high UNION
    SELECT 10, 20 UNION
    SELECT 20, 30 UNION
    SELECT 30, 40 UNION
    SELECT 40, 50 UNION
    SELECT 50, 60 UNION
    SELECT 60, 70 UNION
    SELECT 70, 80 UNION
    SELECT 80, 90 UNION
    SELECT 90, 100
) AS humidity_ranges
WHERE
    weather_dates.avg_humidity BETWEEN humidity_ranges.low AND humidity_ranges.high
GROUP BY
    humidity_ranges.low, humidity_ranges.high;
"""

all_accident_humidity = """
SELECT
    YEAR(weather_dates.day) AS year,
    COUNT(taas.accident_date) AS accident_count,
    SUM(CASE WHEN weather_dates.avg_humidity BETWEEN 0 AND 10 THEN 1 ELSE 0 END) AS humidity_0_10,
    SUM(CASE WHEN weather_dates.avg_humidity BETWEEN 10 AND 20 THEN 1 ELSE 0 END) AS humidity_10_20,
    SUM(CASE WHEN weather_dates.avg_humidity BETWEEN 20 AND 30 THEN 1 ELSE 0 END) AS humidity_20_30,
    SUM(CASE WHEN weather_dates.avg_humidity BETWEEN 30 AND 40 THEN 1 ELSE 0 END) AS humidity_30_40,
    SUM(CASE WHEN weather_dates.avg_humidity BETWEEN 40 AND 50 THEN 1 ELSE 0 END) AS humidity_40_50,
    SUM(CASE WHEN weather_dates.avg_humidity BETWEEN 50 AND 60 THEN 1 ELSE 0 END) AS humidity_50_60,
    SUM(CASE WHEN weather_dates.avg_humidity BETWEEN 60 AND 70 THEN 1 ELSE 0 END) AS humidity_60_70,
    SUM(CASE WHEN weather_dates.avg_humidity BETWEEN 70 AND 80 THEN 1 ELSE 0 END) AS humidity_70_80,
    SUM(CASE WHEN weather_dates.avg_humidity BETWEEN 80 AND 90 THEN 1 ELSE 0 END) AS humidity_80_90,
    SUM(CASE WHEN weather_dates.avg_humidity BETWEEN 90 AND 100 THEN 1 ELSE 0 END) AS humidity_90_100
FROM (
    SELECT DATE(`date`) AS day, ROUND(AVG(CAST(`humidity` AS DECIMAL(5,2))), 2) AS avg_humidity
    FROM weather_new
    WHERE `date` BETWEEN '2007-01-01' AND '2022-12-31'
    GROUP BY day
    HAVING avg_humidity > 0
) AS weather_dates
LEFT JOIN taas_all_data AS taas ON STR_TO_DATE(taas.accident_date, '%Y년 %m월 %d일') = weather_dates.day
GROUP BY YEAR(weather_dates.day)
ORDER BY year;
"""

# df_humidity = pd.DataFrame(gd(humidity_query), columns=['humidity_range_low', 'humidity_range_high', 'days_count'])
df_accident_humidity = pd.DataFrame(gd(all_accident_humidity), columns=['year', 'accident_count', 'humidity_0_10', 'humidity_10_20', 'humidity_20_30', 'humidity_30_40', 'humidity_40_50', 'humidity_50_60', 'humidity_60_70', 'humidity_70_80', 'humidity_80_90', 'humidity_90_100'])

# plt.figure()
# plt.bar(df_humidity['humidity_range_low'], df_humidity['days_count'], width=5, align='edge')
# plt.xticks(range(0, 100, 10))
# plt.xlabel('Humidity')
# plt.ylabel('Days')
# plt.title('Humidity Distribution')
# plt.show()

for i in range(0, 16):
    plt.figure()
    plt.bar(df_accident_humidity['year'], df_accident_humidity.iloc[:, i], width=0.5, align='edge')
    plt.xticks(range(2007, 2023))
    plt.xlabel('Year')
    plt.ylabel('Accident Count')
    plt.title('Accident Count per Year - Humidity ' + str(i*10) + '~' + str(i*10+10))
    plt.show()
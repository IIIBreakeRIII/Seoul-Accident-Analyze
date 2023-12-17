from data_from_server import get_data as gd

import matplotlib.pyplot as plt
import pandas as pd
import calendar

weather_query = """
SELECT
  EXTRACT(YEAR FROM date) AS year,
  EXTRACT(MONTH FROM date) AS month,
  ROUND(AVG(temp), 1) AS avg_temperature
FROM
  weather_new
WHERE
  EXTRACT(YEAR FROM date) BETWEEN 2006 AND 2023
GROUP BY
  EXTRACT(YEAR FROM date),
  EXTRACT(MONTH FROM date)
ORDER BY
  year, month;
"""

all_accident_query = """
SELECT
    SUBSTRING(accident_date, 1, 4) AS year,
    SUBSTRING_INDEX(RIGHT(accident_date, CHAR_LENGTH(accident_date) - 5), '월', 1) AS month, 
    COUNT(*) AS accident_count
FROM
    taas_all_data
WHERE
    accident_date BETWEEN '2006년 1월 1일 00시' AND '2023년 12월 31일 23시'
GROUP BY
    year, month;
"""

condition_accident_query = """
SELECT
    SUBSTRING(accident_date, 1, 4) AS year,
    SUBSTRING_INDEX(RIGHT(accident_date, CHAR_LENGTH(accident_date) - 5), '월', 1) AS month, 
    COUNT(*) AS accident_count
FROM
    taas_condition_data
WHERE
    accident_date BETWEEN '2006년 1월 1일 00시' AND '2023년 12월 31일 23시'
GROUP BY
    year, month;
"""

df_weather = pd.DataFrame(gd(weather_query), columns=['year', 'month', 'avg_temperature'])
df_all_accident = pd.DataFrame(gd(all_accident_query), columns=['year', 'month', 'accident_count'])
df_condition_accident = pd.DataFrame(gd(condition_accident_query), columns=['year', 'month', 'accident_count'])

# Group the data by year and month
grouped_data = df_weather.groupby(['year', 'month']).mean().reset_index()
grouped_all_accident = df_all_accident.groupby(['year', 'month']).sum().reset_index()
grouped_condition_accident = df_condition_accident.groupby(['year', 'month']).sum().reset_index()

# Iterate over the years and create a plot for each year
for year in grouped_all_accident['year'].unique():
  # Filter the data for the current year
  year_all_accident = grouped_all_accident[grouped_all_accident['year'] == year]
  year_condition_accident = grouped_condition_accident[grouped_condition_accident['year'] == year]

  # Convert month column to numeric values
  year_all_accident['month'] = year_all_accident['month'].apply(lambda x: int(x))
  year_condition_accident['month'] = year_condition_accident['month'].apply(lambda x: int(x))

  # Sort the data frame by month column
  year_all_accident = year_all_accident.sort_values('month')
  year_condition_accident = year_condition_accident.sort_values('month')

  # Create a figure with a single subplot
  fig, ax = plt.subplots(figsize=(8, 6))

  # Plot the monthly accident count variation for the current year
  ax.plot(year_all_accident['month'], year_all_accident['accident_count'], label='All Accidents')
  ax.plot(year_condition_accident['month'], year_condition_accident['accident_count'], label='Condition Accidents')
  ax.set_title(f'Accident Count Variation - {year}')
  ax.set_xlabel('Month')
  ax.set_ylabel('Accident Count')
  ax.legend()

  # Set xticks labels as month names
  ax.set_xticks(year_all_accident['month'])
  ax.set_xticklabels([calendar.month_abbr[m] for m in year_all_accident['month']])

  plt.tight_layout()
  plt.show()

# Iterate over the years and create a plot for each year
for year in grouped_data['year'].unique():
  # Filter the data for the current year
  year_data = grouped_data[grouped_data['year'] == year]

  # Create a figure with a single subplot
  fig, ax = plt.subplots(figsize=(8, 6))

  # Plot the monthly temperature variation for the current year
  ax.plot(year_data['month'], year_data['avg_temperature'])
  ax.set_title(f'Temperature Variation - {year}')
  ax.set_xlabel('Month')
  ax.set_ylabel('Temperature (°C)')

  plt.tight_layout()
  plt.show()
from data_from_server import get_data as gd

import matplotlib.pyplot as plt
import pandas as pd

# Condition Data
condition_query = """
SELECT
  CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', -3), '월', 1) AS UNSIGNED) AS month_category,
  
  CASE
    WHEN CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', -1), '시', 1) AS UNSIGNED) BETWEEN 0 AND 6 THEN '0시-6시'
    WHEN CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', -1), '시', 1) AS UNSIGNED) BETWEEN 6 AND 12 THEN '6시-12시'
    WHEN CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', -1), '시', 1) AS UNSIGNED) BETWEEN 12 AND 18 THEN '12시-18시'
    WHEN CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', -1), '시', 1) AS UNSIGNED) BETWEEN 18 AND 23 THEN '18시-00시'
  END AS time_category,

  COUNT(*) AS accident_count
FROM taas_condition_data
GROUP BY month_category, time_category
ORDER BY month_category, time_category;
"""

condtion_df = pd.DataFrame(gd(condition_query))
condtion_df.columns = ["month_category", "time_category", "accident_count"]

condition_count = {}

for i in range(len(condtion_df)):
  if condtion_df.loc[i, "time_category"] == "0시-6시":
    if condtion_df.loc[i, "month_category"] == 12 or condtion_df.loc[i, "month_category"] == 1 or condtion_df.loc[i, "month_category"] == 2:
      if "1q_winter_00-06" in condition_count:
        condition_count["1q_winter_00-06"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["1q_winter_00-06"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 3 or condtion_df.loc[i, "month_category"] == 4 or condtion_df.loc[i, "month_category"] == 5:
      if "2q_spring_00-06" in condition_count:
        condition_count["2q_spring_00-06"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["2q_spring_00-06"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 6 or condtion_df.loc[i, "month_category"] == 7 or condtion_df.loc[i, "month_category"] == 8:
      if "3q_summer_00-06" in condition_count:
        condition_count["3q_summer_00-06"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["3q_summer_00-06"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 9 or condtion_df.loc[i, "month_category"] == 10 or condtion_df.loc[i, "month_category"] == 11:
      if "4q_autumn_00-06" in condition_count:
        condition_count["4q_autumn_00-06"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["4q_autumn_00-06"] = condtion_df.loc[i, "accident_count"]
  elif condtion_df.loc[i, "time_category"] == "6시-12시":
    if condtion_df.loc[i, "month_category"] == 12 or condtion_df.loc[i, "month_category"] == 1 or condtion_df.loc[i, "month_category"] == 2:
      if "1q_winter_06-12" in condition_count:
        condition_count["1q_winter_06-12"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["1q_winter_06-12"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 3 or condtion_df.loc[i, "month_category"] == 4 or condtion_df.loc[i, "month_category"] == 5:
      if "2q_spring_06-12" in condition_count:
        condition_count["2q_spring_06-12"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["2q_spring_06-12"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 6 or condtion_df.loc[i, "month_category"] == 7 or condtion_df.loc[i, "month_category"] == 8:
      if "3q_summer_06-12" in condition_count:
        condition_count["3q_summer_06-12"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["3q_summer_06-12"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 9 or condtion_df.loc[i, "month_category"] == 10 or condtion_df.loc[i, "month_category"] == 11:
      if "4q_autumn_06-12" in condition_count:
        condition_count["4q_autumn_06-12"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["4q_autumn_06-12"] = condtion_df.loc[i, "accident_count"]
  elif condtion_df.loc[i, "time_category"] == "12시-18시":
    if condtion_df.loc[i, "month_category"] == 12 or condtion_df.loc[i, "month_category"] == 1 or condtion_df.loc[i, "month_category"] == 2:
      if "1q_winter_12-18" in condition_count:
        condition_count["1q_winter_12-18"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["1q_winter_12-18"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 3 or condtion_df.loc[i, "month_category"] == 4 or condtion_df.loc[i, "month_category"] == 5:
      if "2q_spring_12-18" in condition_count:
        condition_count["2q_spring_12-18"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["2q_spring_12-18"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 6 or condtion_df.loc[i, "month_category"] == 7 or condtion_df.loc[i, "month_category"] == 8:
      if "3q_summer_12-18" in condition_count:
        condition_count["3q_summer_12-18"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["3q_summer_12-18"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 9 or condtion_df.loc[i, "month_category"] == 10 or condtion_df.loc[i, "month_category"] == 11:
      if "4q_autumn_12-18" in condition_count:
        condition_count["4q_autumn_12-18"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["4q_autumn_12-18"] = condtion_df.loc[i, "accident_count"]
  elif condtion_df.loc[i, "time_category"] == "18시-00시":
    if condtion_df.loc[i, "month_category"] == 12 or condtion_df.loc[i, "month_category"] == 1 or condtion_df.loc[i, "month_category"] == 2:
      if "1q_winter_18-00" in condition_count:
        condition_count["1q_winter_18-00"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["1q_winter_18-00"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 3 or condtion_df.loc[i, "month_category"] == 4 or condtion_df.loc[i, "month_category"] == 5:
      if "2q_spring_18-00" in condition_count:
        condition_count["2q_spring_18-00"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["2q_spring_18-00"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 6 or condtion_df.loc[i, "month_category"] == 7 or condtion_df.loc[i, "month_category"] == 8:
      if "3q_summer_18-00" in condition_count:
        condition_count["3q_summer_18-00"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["3q_summer_18-00"] = condtion_df.loc[i, "accident_count"]
    elif condtion_df.loc[i, "month_category"] == 9 or condtion_df.loc[i, "month_category"] == 10 or condtion_df.loc[i, "month_category"] == 11:
      if "4q_autumn_18-00" in condition_count:
        condition_count["4q_autumn_18-00"] += condtion_df.loc[i, "accident_count"]
      else:
        condition_count["4q_autumn_18-00"] = condtion_df.loc[i, "accident_count"]

print(condition_count)

# All Data
all_query = """
SELECT
  CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', -3), '월', 1) AS UNSIGNED) AS month_category,
  
  CASE
    WHEN CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', -1), '시', 1) AS UNSIGNED) BETWEEN 0 AND 6 THEN '0시-6시'
    WHEN CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', -1), '시', 1) AS UNSIGNED) BETWEEN 6 AND 12 THEN '6시-12시'
    WHEN CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', -1), '시', 1) AS UNSIGNED) BETWEEN 12 AND 18 THEN '12시-18시'
    WHEN CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(accident_date, ' ', -1), '시', 1) AS UNSIGNED) BETWEEN 18 AND 23 THEN '18시-00시'
  END AS time_category,

  COUNT(*) AS accident_count
FROM taas_all_data
GROUP BY month_category, time_category
ORDER BY month_category, time_category;
"""

all_df = pd.DataFrame(gd(all_query))
all_df.columns = ["month_category", "time_category", "accident_count"]

all_count = {}

for i in range(len(all_df)):
  if all_df.loc[i, "time_category"] == "0시-6시":
    if all_df.loc[i, "month_category"] == 12 or all_df.loc[i, "month_category"] == 1 or all_df.loc[i, "month_category"] == 2:
      if "1q_winter_00-06" in all_count:
        all_count["1q_winter_00-06"] += all_df.loc[i, "accident_count"]
      else:
        all_count["1q_winter_00-06"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 3 or all_df.loc[i, "month_category"] == 4 or all_df.loc[i, "month_category"] == 5:
      if "2q_spring_00-06" in all_count:
        all_count["2q_spring_00-06"] += all_df.loc[i, "accident_count"]
      else:
        all_count["2q_spring_00-06"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 6 or all_df.loc[i, "month_category"] == 7 or all_df.loc[i, "month_category"] == 8:
      if "3q_summer_00-06" in all_count:
        all_count["3q_summer_00-06"] += all_df.loc[i, "accident_count"]
      else:
        all_count["3q_summer_00-06"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 9 or all_df.loc[i, "month_category"] == 10 or all_df.loc[i, "month_category"] == 11:
      if "4q_autumn_00-06" in all_count:
        all_count["4q_autumn_00-06"] += all_df.loc[i, "accident_count"]
      else:
        all_count["4q_autumn_00-06"] = all_df.loc[i, "accident_count"]
  elif all_df.loc[i, "time_category"] == "6시-12시":
    if all_df.loc[i, "month_category"] == 12 or all_df.loc[i, "month_category"] == 1 or all_df.loc[i, "month_category"] == 2:
      if "1q_winter_06-12" in all_count:
        all_count["1q_winter_06-12"] += all_df.loc[i, "accident_count"]
      else:
        all_count["1q_winter_06-12"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 3 or all_df.loc[i, "month_category"] == 4 or all_df.loc[i, "month_category"] == 5:
      if "2q_spring_06-12" in all_count:
        all_count["2q_spring_06-12"] += all_df.loc[i, "accident_count"]
      else:
        all_count["2q_spring_06-12"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 6 or all_df.loc[i, "month_category"] == 7 or all_df.loc[i, "month_category"] == 8:
      if "3q_summer_06-12" in all_count:
        all_count["3q_summer_06-12"] += all_df.loc[i, "accident_count"]
      else:
        all_count["3q_summer_06-12"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 9 or all_df.loc[i, "month_category"] == 10 or all_df.loc[i, "month_category"] == 11:
      if "4q_autumn_06-12" in all_count:
        all_count["4q_autumn_06-12"] += all_df.loc[i, "accident_count"]
      else:
        all_count["4q_autumn_06-12"] = all_df.loc[i, "accident_count"]
  elif all_df.loc[i, "time_category"] == "12시-18시":
    if all_df.loc[i, "month_category"] == 12 or all_df.loc[i, "month_category"] == 1 or all_df.loc[i, "month_category"] == 2:
      if "1q_winter_12-18" in all_count:
        all_count["1q_winter_12-18"] += all_df.loc[i, "accident_count"]
      else:
        all_count["1q_winter_12-18"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 3 or all_df.loc[i, "month_category"] == 4 or all_df.loc[i, "month_category"] == 5:
      if "2q_spring_12-18" in all_count:
        all_count["2q_spring_12-18"] += all_df.loc[i, "accident_count"]
      else:
        all_count["2q_spring_12-18"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 6 or all_df.loc[i, "month_category"] == 7 or all_df.loc[i, "month_category"] == 8:
      if "3q_summer_12-18" in all_count:
        all_count["3q_summer_12-18"] += all_df.loc[i, "accident_count"]
      else:
        all_count["3q_summer_12-18"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 9 or all_df.loc[i, "month_category"] == 10 or all_df.loc[i, "month_category"] == 11:
      if "4q_autumn_12-18" in all_count:
        all_count["4q_autumn_12-18"] += all_df.loc[i, "accident_count"]
      else:
        all_count["4q_autumn_12-18"] = all_df.loc[i, "accident_count"]
  elif all_df.loc[i, "time_category"] == "18시-00시":
    if all_df.loc[i, "month_category"] == 12 or all_df.loc[i, "month_category"] == 1 or all_df.loc[i, "month_category"] == 2:
      if "1q_winter_18-00" in all_count:
        all_count["1q_winter_18-00"] += all_df.loc[i, "accident_count"]
      else:
        all_count["1q_winter_18-00"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 3 or all_df.loc[i, "month_category"] == 4 or all_df.loc[i, "month_category"] == 5:
      if "2q_spring_18-00" in all_count:
        all_count["2q_spring_18-00"] += all_df.loc[i, "accident_count"]
      else:
        all_count["2q_spring_18-00"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 6 or all_df.loc[i, "month_category"] == 7 or all_df.loc[i, "month_category"] == 8:
      if "3q_summer_18-00" in all_count:
        all_count["3q_summer_18-00"] += all_df.loc[i, "accident_count"]
      else:
        all_count["3q_summer_18-00"] = all_df.loc[i, "accident_count"]
    elif all_df.loc[i, "month_category"] == 9 or all_df.loc[i, "month_category"] == 10 or all_df.loc[i, "month_category"] == 11:
      if "4q_autumn_18-00" in all_count:
        all_count["4q_autumn_18-00"] += all_df.loc[i, "accident_count"]
      else:
        all_count["4q_autumn_18-00"] = all_df.loc[i, "accident_count"]

print(all_count)

# Compare By pyplot
# Get the keys and values from the dictionaries
all_keys = list(all_count.keys())
all_values = list(all_count.values())
condition_values = list(condition_count.values())

# Plot the data
plt.plot(all_keys, all_values, label='all_count')
plt.plot(all_keys, condition_values, label='condition_count')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('all_count and condition_count')
plt.xticks(rotation=90)

# Add legend
plt.legend()

# Show the plot
plt.show()
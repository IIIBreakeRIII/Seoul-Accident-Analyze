from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 날씨 데이터 가져오기
weather_query = """
SELECT date, AVG(temp) as avg_temperature
FROM weather
GROUP BY date
"""

weather_result = gd(weather_query)
weather_df = pd.DataFrame(weather_result, columns=['date', 'avg_temperature'])
# , format='%Y년 %m월 %d일 %H시', errors='coerce')
# weather_df['year'] = weather_df['date'].dt.year
# weather_df['month'] = weather_df['date'].dt.month


# 사고 데이터 가져오기
accident_query = """
SELECT accident_date, road_condition
FROM taas_all_data
"""

accident_result = gd(accident_query)
accident_df = pd.DataFrame(accident_result, columns=['accident_date', 'road_condition'])

# 데이터 전처리
accident_df.dropna(subset=['road_condition'], inplace=True)
accident_df['accident_date'] = pd.to_datetime(accident_df['accident_date'], format='%Y년 %m월 %d일 %H시', errors='coerce')
accident_df['year'] = accident_df['accident_date'].dt.year
accident_df['month'] = accident_df['accident_date'].dt.month

# 월별 사고 건수 계산
monthly_accident_counts = accident_df.groupby(['year', 'month', 'road_condition']).size().reset_index(name='count')

# 전체 사고 건수 대비 각 노면상태별 사고 비율 계산
monthly_accident_ratios = monthly_accident_counts.pivot_table(values='count', index=['year', 'month'], columns='road_condition', aggfunc='sum')
monthly_accident_ratios = monthly_accident_ratios.div(monthly_accident_ratios.sum(axis=1), axis=0) * 100

# 날씨와 사고 데이터 병합
merged_df = pd.merge(weather_df, monthly_accident_ratios, how='inner', left_on=['date'], right_on=['year', 'month'])
merged_df.drop(['year', 'month'], axis=1, inplace=True)

# 그래프 그리기
plt.figure(figsize=(15, 8))

# 평균기온 선 그래프
plt.plot(merged_df['date'], merged_df['avg_temperature'], marker='o', label='평균기온')

# 각 노면상태에 대한 선 그래프 생성
for road_condition in monthly_accident_ratios.columns:
    plt.plot(merged_df['date'], merged_df[road_condition], marker='o', label=road_condition)

plt.rc('font', family='Malgun Gothic')
plt.title('월별 평균기온 및 노면상태별 사고 비율')
plt.xlabel('날짜')
plt.ylabel('비율 또는 기온')
plt.legend(title='요소', loc='upper right', bbox_to_anchor=(1.1, 1))
plt.grid(True)
plt.show()
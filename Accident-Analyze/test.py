from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

# SQL 쿼리를 이용하여 데이터 가져오기
query = """
SELECT taas_all_data.accident_date, taas_all_data.road_condition, weather.temp
FROM taas.taas_all_data
LEFT JOIN weather ON taas_all_data.accident_date = weather.date
"""

result = gd(query)
df = pd.DataFrame(result, columns=['accident_date', 'road_condition', 'temp'])

# 시간대별 온도를 하루 중 최고 온도로 처리
df['accident_date'] = pd.to_datetime(df['accident_date'], format='%Y년 %m월 %d일 %H시', errors='coerce')
df['weather_date'] = df['accident_date'].dt.strftime('%Y-%m-%d %H:%M')
df['hour'] = df['accident_date'].dt.hour
df['max_temp'] = df.groupby(['weather_date', 'road_condition'])['temp'].transform('max')
df = df.drop_duplicates(['weather_date', 'road_condition'])

# 년도와 월을 나누어 열로 추가
df['year'] = df['accident_date'].dt.year
df['month'] = df['accident_date'].dt.month

# 월별 평균 온도 계산
monthly_avg_temp = df.groupby(['year', 'month'])['max_temp'].mean().reset_index(name='avg_temp')

# 월별 노면상태별 사고 건수 계산
monthly_road_condition_counts = df.groupby(['year', 'month', 'road_condition']).size().reset_index(name='count')

# 전체 사고 건수 대비 각 노면상태별 사고 비율 계산
monthly_road_condition_ratios = monthly_road_condition_counts.pivot_table(values='count', index=['year', 'month'], columns='road_condition', aggfunc='sum')
monthly_road_condition_ratios = monthly_road_condition_ratios.div(monthly_road_condition_ratios.sum(axis=1), axis=0) * 100

# 그래프 그리기
plt.figure(figsize=(15, 8))

plt.rc('font', family='Malgun Gothic')
# 월별 평균 온도 그래프
plt.plot(monthly_avg_temp.index, monthly_avg_temp['avg_temp'], marker='o', label='월별 평균 온도')

# 각 노면상태에 대한 선 그래프 생성
for road_condition in monthly_road_condition_ratios.columns:
    plt.plot(monthly_road_condition_ratios.index, monthly_road_condition_ratios[road_condition].values, marker='o', label=road_condition)    

plt.title('월별 평균 온도 및 노면상태별 사고 비율')
plt.xlabel('연도-월')
plt.ylabel('사고 비율 (%)')
plt.legend(title='노면상태', loc='upper right', bbox_to_anchor=(1.2, 1))
plt.grid(True)
plt.show()

from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

# SQL 쿼리를 이용하여 데이터 가져오기
query = """
SELECT accident_date, road_condition
FROM taas_condition_data
"""

# 데이터 불러오기
result = gd(query)

# 데이터프레임 생성
df = pd.DataFrame(result, columns=['accident_date', 'road_condition'])

# road_condition이 NaN인 행 제거
df.dropna(subset=['road_condition'], inplace=True)

# 연도와 월을 나누어 열로 추가
df['accident_date'] = pd.to_datetime(df['accident_date'], format='%Y년 %m월 %d일 %H시', errors='coerce')
df['year'] = df['accident_date'].dt.year
df['month'] = df['accident_date'].dt.month

# 월별 노면상태별 사고 건수 계산
monthly_road_condition_counts = df.groupby(['year', 'month', 'road_condition']).size().reset_index(name='count')

# 월별 평균 노면상태별 사고 건수 계산
monthly_road_condition_means = monthly_road_condition_counts.groupby('month')['count'].mean().reset_index()

# 전체 사고 건수 대비 각 노면상태별 사고 비율 계산
monthly_road_condition_ratios = monthly_road_condition_counts.pivot_table(values='count', index=['year', 'month'], columns='road_condition', aggfunc='sum')

# 비율로 변환
monthly_road_condition_ratios = monthly_road_condition_ratios.div(monthly_road_condition_ratios.sum(axis=1), axis=0) * 100

# MultiIndex를 일반적인 형태로 변환
monthly_road_condition_ratios = monthly_road_condition_ratios.reset_index()

# 그래프 그리기
plt.figure(figsize=(15, 8))
plt.rc('font', family='Malgun Gothic')

# 각 노면상태에 대한 선 그래프 생성
for road_condition in monthly_road_condition_ratios.columns[2:]:
    plt.plot(monthly_road_condition_means['month'], monthly_road_condition_ratios.groupby('month')[road_condition].mean(), 
             marker='o', label=road_condition)

plt.title('월별 평균 노면상태별 사고 비율 (조건)')
plt.xlabel('월')
plt.ylabel('평균 사고 비율 (%)')
plt.legend(title='노면상태', loc='upper right', bbox_to_anchor=(1.1, 1))
plt.xticks(range(1, 13))
plt.grid(True)
plt.show()
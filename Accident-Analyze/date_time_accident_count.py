from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

# 예시로 사용된 쿼리이므로 실제 데이터에 맞게 수정해야 합니다.
query_all = """
SELECT accident_date, COUNT(*) as count
FROM taas.taas_all_data
GROUP BY accident_date
"""
query_condition = """
SELECT accident_date, COUNT(*) as count
FROM taas.taas_condition_data
GROUP BY accident_date
"""
# 데이터베이스에서 데이터 불러오기


# 불러온 데이터를 DataFrame으로 변환
df_all = pd.DataFrame(gd(query_all), columns=['accident_date', 'count'])
df_condition = pd.DataFrame(gd(query_condition), columns=['accident_date', 'count'])

# 'accident_date' 열을 직접 지정한 날짜 형식으로 변환
df_all['accident_date'] = pd.to_datetime(df_all['accident_date'], format='%Y년 %m월 %d일 %H시', errors='coerce')
df_condition['accident_date'] = pd.to_datetime(df_condition['accident_date'], format='%Y년 %m월 %d일 %H시', errors='coerce')

# 'hour' 열을 추가하여 시간대 정보 추출
df_all['hour'] = df_all['accident_date'].dt.hour
df_condition['hour'] = df_condition['accident_date'].dt.hour

# 시간대별 사고 데이터 수 계산
hourly_all_counts = df_all.groupby('hour')['count'].sum()
hourly_condition_counts = df_condition.groupby('hour')['count'].sum()

# 그래프 그리기
plt.figure(figsize=(15, 6))
plt.plot(hourly_all_counts.index, hourly_all_counts.values, marker='o', color='blue', linestyle='-')
plt.plot(hourly_condition_counts.index, hourly_condition_counts.values, marker='o', color='red', linestyle='-')
plt.xlabel('시간대')
plt.ylabel('사고 건수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('시간대별 사고 건수')
plt.xticks(range(24))  # x 축에 시간대 표시
plt.tight_layout()
plt.show()
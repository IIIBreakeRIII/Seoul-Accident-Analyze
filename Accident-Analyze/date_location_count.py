from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# SQL 쿼리를 이용하여 데이터 가져오기
query = """
SELECT accident_date, location
FROM taas.taas_condition_data
"""

# 데이터 불러오기
result = gd(query)

# 데이터프레임 생성
df = pd.DataFrame(result, columns=['accident_date', 'location'])

# 강남구 제외
df = df[df['location'].str.contains('강남구') == False]
df = df[df['location'].str.contains('송파구') == False]

# accident_date를 datetime 형식으로 변환
df['accident_date'] = pd.to_datetime(df['accident_date'], format='%Y년 %m월 %d일 %H시', errors='coerce')

# 시간대와 지역에 따른 사고 건수 계산
df['year'] = df['accident_date'].dt.year
df['location_gu'] = df['location'].apply(lambda x: ' '.join(x.split(' ')[1:2]))

# Pivot을 이용하여 시간대와 지역(구)에 따른 사고 건수 구하기
hourly_location_gu_counts = df.pivot_table(index='year', columns='location_gu', aggfunc='size', fill_value=0)

print(hourly_location_gu_counts)
plt.figure(figsize=(15, 8))
sns.heatmap(hourly_location_gu_counts, cmap='Reds', cbar_kws={'label': 'Accident Count'})
plt.title('연도별과 지역(구)에 따른 사고 건수(강남구, 송파구 제외)')
plt.xlabel('지역(구)')
plt.ylabel('연도')
plt.show()

#(강남구, 송파구 제외)
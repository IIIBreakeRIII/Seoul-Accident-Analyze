from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

# SQL 쿼리를 이용하여 데이터 가져오기
query = """
SELECT accident_date, location
FROM taas_all_data
"""

# 데이터 불러오기
result = gd(query)

# 데이터프레임 생성
df = pd.DataFrame(result, columns=['accident_date', 'location'])

# '미분류'를 NaN 값으로 대체하고, NaN 값을 가진 행 삭제
df['location'] = df['location'].replace('미분류', pd.NA)
df = df.dropna(subset=['location'])

# '서울특별시' 부분을 제거하고 '구'까지만 추출
df['location'] = df['location'].apply(lambda x: x.split(' ')[-2] if ' ' in x else x)

# accident_date를 datetime 형식으로 변환
df['accident_date'] = pd.to_datetime(df['accident_date'], format='%Y년 %m월 %d일 %H시', errors='coerce')

# 연도와 월을 나누어 열로 추가
df['year'] = df['accident_date'].dt.year
df['month'] = df['accident_date'].dt.month

# 월별 지역별 사고 건수 계산
monthly_location_counts = df.groupby(['year', 'month', 'location']).size().reset_index(name='count')

# 월별 지역별 사고 건수 그래프
plt.figure(figsize=(15, 8))

# 각 지역별로 색상 구분 
colors = plt.cm.tab20.colors

# 각 지역에 대한 막대 그래프 생성
for i, location in enumerate(monthly_location_counts['location'].unique()):
    location_data = monthly_location_counts[monthly_location_counts['location'] == location]
    plt.bar(location_data['month'] + i * 0.2, location_data['count'], width=0.2, label=location, color=colors[i])

plt.title('Accident Count by Month and Location')
plt.xlabel('Month')
plt.ylabel('Accident Count')

# 범례에 표시될 순서를 설정
plt.legend(title='Location', loc='upper right', bbox_to_anchor=(1.1, 1), ncol=2)
plt.show()
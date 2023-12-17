from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

query = """
SELECT accident_date, COUNT(*) as count
FROM taas.taas_condition_data
GROUP BY accident_date
"""

# 불러온 데이터를 DataFrame으로 변환
accident_date_count = pd.DataFrame(gd(query), columns=['accident_date', 'count'])

# 'accident_date' 열을 datetime 형식으로 변환
accident_date_count['accident_date'] = pd.to_datetime(accident_date_count['accident_date'], format='%Y년 %m월 %d일 %H시', errors='coerce')

# 2007년부터 2010년까지의 데이터만 선택
accident_date_count_selected = accident_date_count[(accident_date_count['accident_date'] >= '2007-01-01') & (accident_date_count['accident_date'] <= '2022-12-31')]

# 'accident_date' 열에서 월 정보를 추출하여 'month' 열 추가
#accident_date_count_selected['month'] = accident_date_count_selected['accident_date'].dt.to_period('M')
accident_date_count_selected['year'] = accident_date_count_selected['accident_date'].dt.to_period('Y')

# 월별 사고 데이터 수 계산
#monthly_counts = accident_date_count_selected.groupby('month')['count'].sum()
yearly_counts = accident_date_count_selected.groupby('year')['count'].sum()

# 그래프 그리기
plt.figure(figsize=(15, 6))

#plt.bar(monthly_counts.index.astype(str), monthly_counts.values, color='green')
#plt.plot(monthly_counts.index.astype(str), monthly_counts.values, marker='o', color='green', linestyle='-')

plt.bar(yearly_counts.index.astype(str), yearly_counts.values, color='red')


plt.xlabel('연도')
plt.ylabel('사고 건수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('2007년부터 2022년까지 연도별 사고 건수(조건)')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()
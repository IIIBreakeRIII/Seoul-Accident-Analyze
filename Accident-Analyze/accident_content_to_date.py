from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 예시로 사용된 쿼리이므로 실제 데이터에 맞게 수정해야 합니다.
query = """
SELECT accident_date, accident_content, COUNT(*) as count
FROM taas.taas_condition_data
GROUP BY accident_date, accident_content
"""

# 데이터베이스에서 데이터 불러오기
result = gd(query)

# 불러온 데이터를 DataFrame으로 변환
df = pd.DataFrame(result, columns=['accident_date', 'accident_content', 'count'])

# 'accident_date' 열을 직접 지정한 날짜 형식으로 변환
df['accident_date'] = pd.to_datetime(df['accident_date'], format='%Y년 %m월 %d일 %H시', errors='coerce')

# 'year' 열을 추가하여 년도 정보 추출
df['year'] = df['accident_date'].dt.year

yearly_counts = df.groupby(['year', 'accident_content'])['count'].sum().unstack()
print(yearly_counts)

# seaborn을 활용하여 그래프 그리기
yearly_counts.plot(kind='bar', stacked=True, figsize=(15, 6))
#sns.lineplot(x='year', y='count', hue='accident_content', data=df, size='accident_content')
plt.xlabel('년도')
plt.ylabel('사고 건수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('년도별 사고 유형별 건수')
plt.tight_layout()
plt.show()
from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

query = """
SELECT weekday, accident_content, COUNT(*) as count
FROM taas.taas_condition_data
GROUP BY weekday, accident_content
"""

# 불러온 데이터를 DataFrame으로 변환
df = pd.DataFrame(gd(query), columns=['weekday', 'accident_content', 'count'])

weekday_order = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
df['weekday'] = pd.Categorical(df['weekday'], categories=weekday_order, ordered=True)

# 요일별 사고 유형 데이터 수 계산
weekday_counts = df.groupby(['weekday', 'accident_content'])['count'].sum().unstack()

print(weekday_counts)

# 그래프 그리기
weekday_counts.plot(kind='bar', stacked=True, figsize=(15, 6))
plt.xlabel('요일')
plt.ylabel('사고 건수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('요일별 사고 유형별 건수')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

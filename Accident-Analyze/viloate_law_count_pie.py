from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

# SQL 쿼리를 이용하여 데이터 가져오기
query = """
SELECT violate_law, COUNT(*) as count
FROM taas_all_data
WHERE violate_law IS NOT NULL
GROUP BY violate_law
"""

# 데이터 불러오기
result = gd(query)

# 데이터프레임 생성
df = pd.DataFrame(result, columns=['violate_law', 'count'])

# 비율 계산
df['ratio'] = df['count'] / df['count'].sum() * 100
df = df.sort_values(by='ratio', ascending=False)


# 원형 그래프 그리기

plt.figure(figsize=(8, 8))
plt.rc('font', family='Malgun Gothic')
plt.pie(df['ratio'], labels=df['violate_law'], autopct='%1.1f%%', startangle=90, counterclock=False)
plt.title('법규위반 비율')
plt.show()

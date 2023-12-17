from gm_data import get_data as gd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# SQL 쿼리를 이용하여 데이터 가져오기
query = """
SELECT location, COUNT(*) as count
FROM taas.taas_all_data
WHERE location != '미분류 미분류 미분류'
"""

# 데이터 불러오기
result = gd(query)

# 데이터프레임 생성
df = pd.DataFrame(result, columns=['location', 'count'])

# '00구'까지만 남기기
df['구'] = df['location'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)
print(df['구'])
# 시각화
plt.figure(figsize=(15, 8))
plt.rc('font', family='Malgun Gothic')
sns.barplot(x='구', y='count', data=df, palette='viridis')
plt.title('지역별 전체 사고 건수')
plt.xlabel('구')
plt.ylabel('전체 사고 건수')
plt.show()
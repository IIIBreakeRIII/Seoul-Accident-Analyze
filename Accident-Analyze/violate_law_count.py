from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

# SQL 쿼리를 이용하여 데이터 가져오기
query = """
SELECT violate_law
FROM taas_condition_data
"""

# 데이터 불러오기
result = gd(query)
df = pd.DataFrame(result, columns=['violate_law'])

# 법규위반별 사고 건수 계산
violate_law_counts = df['violate_law'].value_counts()

# 전체 사고 건수 대비 법규위반별 사고 비율 계산
violate_law_ratios = violate_law_counts / violate_law_counts.sum() * 100

# 그래프 그리기
plt.figure(figsize=(17, 6))
plt.rc('font', family='Malgun Gothic')
violate_law_ratios.plot(kind='bar', color='skyblue')
plt.title('법규위반별 사고 비율(조건)')
plt.xlabel('법규위반')
plt.ylabel('사고 비율 (%)')
plt.xticks(range(len(violate_law_ratios.index)), [label[:10] for label in violate_law_ratios.index], rotation=0)

# 그래프에 수치 표시
for i, v in enumerate(violate_law_ratios):
    plt.text(i, v + 0.5, f'{v:.1f}%', ha='center', va='bottom')
plt.show()

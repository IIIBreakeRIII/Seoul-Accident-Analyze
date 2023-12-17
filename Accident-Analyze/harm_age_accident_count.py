from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

# 예시로 사용된 쿼리이므로 실제 데이터에 맞게 수정해야 합니다.
query = """
SELECT harm_age, accident_content, COUNT(*) as count
FROM taas.taas_condition_data
GROUP BY harm_age, accident_content
"""

query_all ="""
SELECT harm_age, accident_content, COUNT(*) as count
FROM taas.taas_all_data
GROUP BY harm_age, accident_content
"""
# 데이터베이스에서 데이터 불러오기
result = gd(query)

# 불러온 데이터를 DataFrame으로 변환
df = pd.DataFrame(result, columns=['harm_age', 'accident_content', 'count'])
df_all = pd.DataFrame(gd(query_all),columns=['harm_age', 'accident_content', 'count'])
# '세' 제거하고 정수형으로 변환
df['harm_age'] = df['harm_age'].str.replace('세', '').str.replace('이상', '').replace('기타불명', float('nan')).replace('미분류',float('nan')).astype(float)
df_all['harm_age'] = df_all['harm_age'].str.replace('세', '').str.replace('이상', '').replace('기타불명', float('nan')).replace('미분류',float('nan')).astype(float)

total_accidents = df_all['count'].sum()
accidents_65_over = df[df['harm_age'] >= 65]['count'].sum()
ratio_65_over = accidents_65_over / total_accidents

# 나이대를 나타내는 새로운 칼럼 추가
df['age_group'] = pd.cut(df['harm_age'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], right=False, labels=['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99'])

# 각 나이대별로 accident_content의 카운트 출력
age_group_counts = df.groupby(['age_group', 'accident_content'])['count'].sum().unstack()

print(age_group_counts)
print("-------------------------------")
print(f"65세 이상의 조건부 전체 사고 수: {accidents_65_over}")
print(f"전체 사고 수에서 65세 이상의 조건부 사고 비율: {ratio_65_over * 100:.2f}%")

# 각 나이대별로 accident_content의 카운트 그래프로 출력

age_group_counts.plot(kind='bar', stacked=True, figsize=(15, 6))
plt.xlabel('나이대')
plt.ylabel('사고 건수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('나이대별 사고 유형별 건수')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

# SQL 쿼리를 이용하여 데이터 가져오기
query = """
SELECT accident_date, road_condition
FROM taas.taas_all_data
"""

# 데이터 불러오기
result = gd(query)

# 데이터프레임 생성
df = pd.DataFrame(result, columns=['accident_date', 'road_condition'])

# road_condition이 NaN인 행 제거
df.dropna(subset=['road_condition'], inplace=True)

# 각 노면상태별 사고 건수 계산
road_condition_counts = df['road_condition'].value_counts()

# 전체 사고 건수 대비 각 노면상태별 사고 비율 계산
road_condition_ratios = road_condition_counts / len(df) * 100
print(road_condition_ratios)
# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.rc('font', family='Malgun Gothic')
road_condition_ratios.plot(kind='bar', color='skyblue')
plt.xlabel('노면상태')
plt.ylabel('사고 비율 (%)')
plt.title('노면상태별 사고 비율(전체)')
plt.show()
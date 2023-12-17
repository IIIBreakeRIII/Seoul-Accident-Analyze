from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

# 예시로 사용된 쿼리이므로 실제 데이터에 맞게 수정해야 합니다.
query = """
SELECT location, accident_content, COUNT(*) as count
FROM taas.taas_condition_data
GROUP BY location, accident_content
"""

# 데이터베이스에서 데이터 불러오기
result = gd(query)

# 불러온 데이터를 DataFrame으로 변환
df = pd.DataFrame(result, columns=['location', 'accident_content', 'count'])

# 'gu' 열을 추가하여 구 정보 추출
df['gu'] = df['location'].str.extract('서울특별시 (.+?)구')

# 각 구별로 accident_content의 카운트 출력
gu_counts = df.groupby(['gu', 'accident_content'])['count'].sum().unstack()
print(gu_counts)

# 각 구별로 accident_content의 카운트 그래프로 출력
gu_counts.plot(kind='bar', stacked=True)
plt.xlabel('구')
plt.ylabel('사고 건수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('서울특별시 각 구별 사고 유형별 건수')
plt.xticks(rotation=45, ha='right')

plt.xticks(range(len(gu_counts.index)), [gu + '구' for gu in gu_counts.index])

plt.tight_layout()
plt.show()

##노인의 운전면허증을 뺐어야되는 이유 
##원동기를 딸수 있는 나이 뭐시기저시기
# ## 시간대별 위치 에 따른 사고 예측?
# 교통사고 자체 데이터
# 1. 나이대별 데이터 분석 (사고 비율)
# 1.1. 노인 사고율이 얼마나 영향을 끼치는지(가해자로만 분석) 면허 뺏어 말어
# 2. (어떠한 기준 속에서)사고라는건 예견이 된다.
# 3. 가장 많이 일어나는 사고 유형(위반 사항)
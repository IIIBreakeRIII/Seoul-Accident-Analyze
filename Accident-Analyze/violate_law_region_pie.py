from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# matplotlib에서 한글 폰트 사용 설정
plt.rc('font', family='Malgun Gothic')

# SQL 쿼리를 이용하여 데이터 가져오기
query = """
SELECT location, violate_law, COUNT(*) as count
FROM taas_all_data
WHERE location IS NOT NULL AND location != '미분류 미분류 미분류'
GROUP BY location, violate_law
"""

result = gd(query)

# 데이터프레임 생성
df = pd.DataFrame(result, columns=['location', 'violate_law', 'count'])

# '00구'까지만 남기기
df['district'] = df['location'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else x)

# 각 구와 법규 위반 유형별 사건 수 계산
district_violation = df.groupby(['district', 'violate_law'])['count'].sum().reset_index()

# 모든 '구'의 리스트 생성
districts = df['district'].unique()

# 전체 '구'에서 가장 많이 발생한 법규 위반 유형 순서를 기준으로 정렬
violate_law_order = df.groupby('violate_law')['count'].sum().sort_values(ascending=False).index

# 법규 위반 유형별로 다른 색상의 선 그리기
plt.figure(figsize=(15, 8))

for district in districts:
    # 해당 '구'의 데이터만 선택
    sub_df = district_violation[district_violation['district'] == district]

    # 전체 '구'에서 가장 많이 발생한 법규 위반 유형 순서를 기준으로 데이터프레임 재정렬
    sub_df = sub_df.set_index('violate_law').reindex(violate_law_order).reset_index()
    
    # 꼭짓점 그래프 그리기
    plt.plot(sub_df['violate_law'], sub_df['count'], marker='o', label=district)

# 범례 추가
plt.legend()

# 그래프 제목 및 축 이름 설정
plt.title('각 구의 법규 위반 비율')
plt.xlabel('법규 위반 유형')
plt.ylabel('비율')

# x축 라벨 회전
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

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

# '구' 별 총 사건 수 계산
total_counts = district_violation.groupby('district')['count'].sum()

# 모든 '구'와 '법규 위반 유형'의 리스트 생성
districts = df['district'].unique()
violate_laws = df['violate_law'].unique()

# '법규 위반 유형'별로 다른 색상의 선 그리기
plt.figure(figsize=(15, 8))

for violate_law in violate_laws:
    # 해당 '법규 위반 유형'의 데이터만 선택
    sub_df = district_violation[district_violation['violate_law'] == violate_law]

    # '구' 별 사건 수를 총 사건 수로 나누어 비율 계산
    sub_df['count'] = sub_df.apply(lambda row: row['count'] / total_counts[row['district']], axis=1)

    # '구' 순서를 기준으로 데이터프레임 재정렬
    sub_df = sub_df.set_index('district').reindex(districts).reset_index()
    
    # 꼭짓점 그래프 그리기
    plt.plot(sub_df['district'], sub_df['count'], marker='o', label=violate_law)

# 범례 추가
plt.legend()

# 그래프 제목 및 축 이름 설정
plt.title('각 구의 법규 위반 사건 수(전체)')
plt.xlabel('구')
plt.ylabel('비율 (%)')

# x축 라벨 회전
plt.xticks(rotation=90)
plt.grid()
plt.tight_layout()
plt.show()

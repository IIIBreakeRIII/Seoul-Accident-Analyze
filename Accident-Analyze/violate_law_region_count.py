from gm_data import get_data as gd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 서울의 특정 '구' 리스트
region = ['도봉구', '강북구', '노원구', '은평구', '마포구', '서대문구', '종로구', '성북구', '중랑구', '동대문구', '중구', '용산구', '성동구', '광진구', '강동구', '송파구',
          '강남구', '서초구', '동작구', '관악구', '금천구', '영등포구', '구로구', '양천구', '강서구']

region_violate_ratios = []

for index in region:
    # 법규위반 비율 쿼리
    query = """
    SELECT violate_law, COUNT(*) as count
    FROM taas.taas_all_data
    WHERE location LIKE '%{}%' AND violate_law IS NOT NULL AND violate_law != '미분류 미분류 미분류'
    GROUP BY violate_law
    """.format(index)
    
    result = gd(query)
    df = pd.DataFrame(result, columns=['violate_law', 'count'])
    
    # 법규위반 비율 계산
    total_count = df['count'].sum()
    df['ratio'] = df['count'] / total_count * 100
    
    # '구' 정보 추가
    df['구'] = index
    region_violate_ratios.append(df)

# 데이터프레임 통합
region_violate_ratios_df = pd.concat(region_violate_ratios)

pivot_df = region_violate_ratios_df.pivot(index='violate_law', columns='구', values='ratio')


# 시각화
plt.figure(figsize=(15, 8))
plt.rc('font', family='Malgun Gothic')
#sns.barplot(x='구', y='ratio', hue='violate_law', data=region_violate_ratios_df, palette='viridis')
sns.heatmap(pivot_df, annot=True, cmap='viridis', fmt=".1f", linewidths=.5)

plt.title('지역별 법규위반 비율')
plt.xlabel('지역')
plt.ylabel('비율 (%)')
plt.legend(title='법규위반', loc='upper right', bbox_to_anchor=(1, 1))
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()

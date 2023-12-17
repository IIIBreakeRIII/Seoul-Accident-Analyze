from gm_data import get_data as gd
import pandas as pd
import matplotlib.pyplot as plt

region =['도봉구','강북구', '노원구', '은평구', '마포구', '서대문구', '종로구', '성북구', '중랑구', '동대문구', '중구', '용산구' , '성동구', '광진구', '강동구', '송파구',
          '강남구', '서초구', '동작구','관악구', '금천구', '영등포구', '구로구', '양천구', '강서구']

region_all_count = {}
region_condition_count = {}

for index in region:
    count_all = gd("SELECT COUNT(*) FROM taas.taas_all_data WHERE location LIKE '%{}%'".format(index))
    count_condition = gd("SELECT COUNT(*) FROM taas.taas_condition_data WHERE location LIKE '%{}%'".format(index))
    count_all = int(count_all[0][0])
    count_condition =int(count_condition[0][0])
    region_all_count[index] = count_all
    region_condition_count[index] = count_condition
print(region_all_count)
print(region_condition_count)

##region_counts = pd.DataFrame(gd(query), columns=['location', 'count'])

plt.figure(figsize=(15, 6))
plt.rc('font', family='Malgun Gothic')
# plt.bar를 사용하여 막대 그래프 그리기

plt.bar(region_all_count.keys(), region_all_count.values(), color='blue')
plt.xlabel('지역')
plt.ylabel('사고 건수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('서울 지역별 사고 건수(전체)')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()

plt.bar(region_condition_count.keys(), region_condition_count.values(), color='red')
plt.xlabel('지역')
plt.ylabel('사고 건수')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.title('서울 지역별 사고 건수(조건)')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()
"""
SQL Server에서 Pandas Dataframe으로 데이터를 가져오는 방법을 설명합니다.
이 코드를 기반으로 각자 새로운 코드를 작성하세요.

흐름은 다음과 같습니다.

1. SQL Server에 접속합니다.
2. 함수의 파라미터로 SQL Query를 받습니다.
3. 데이터를 리턴하고 서버를 종료합니다.
4. 데이터를 데이터프레임으로 변환합니다.

-- 주의 사항 --
개인이 서버에서 작업한 후, 작업 코드 및 코드 내역을 Github에 올리지 않도록 주의하세요.
!! IP 및 개인정보가 있기 때문에 Github에 올리면 안됩니다. !!
파일을 따로 분리해서 이 코드를 제외하고 올리거나, .gitignore를 이용하세요.

-- .gitignore 사용법 --
1. 해당 레포지토리에 .gitignore 파일을 엽니다.
2. # Ignore db server file 밑에 파일 이름과 확장자를 적습니다.
  2.1. 예시 : csv_to_SQL_Server.py
3. .gitignore 파일을 저장합니다.
4. git rm -r --cached ., git init, git add ., git commit -m "message", git push를 합니다.

위 과정을 거치지 않을 경우, 개인정보가 노출될 수 있습니다.
또한, 레포지토리 소유자가 해당 파일을 임의로 삭제할 수 있습니다.
"""

import pymysql.cursors
import pandas as pd

def get_data(sql_query):
  connect = pymysql.connect(host='Server Address', port=0, user='User ID', password='User PW', db='Schema Name', charset='charcter set')
  cursor = connect.cursor()
  query = sql_query
  cursor.execute(query)

  result = cursor.fetchall()
  connect.close()

  return result

# SQL to DataFrame
all_df = pd.DataFrame(get_data("SQL Query"))
condition_df = pd.DataFrame(get_data("SQL Query"))

print(all_df.shape)
print(condition_df.shape)
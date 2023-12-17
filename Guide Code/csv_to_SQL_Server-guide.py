"""
CSV 파일을 SQL Server에 넣는 방법을 설명합니다.
이 코드를 기반으로 각자 새로운 코드를 작성하세요.

흐름은 다음과 같습니다.

1. SQL Server에 접속합니다.
2. CSV 파일을 읽습니다.
3. CSV 파일의 데이터를 SQL Server에 넣습니다.
4. SQL Server와의 연결을 끊습니다.

-- 주의 사항 --
개인이 서버에 파일을 올린 후, 작업 코드 및 코드 내역을 Github에 올리지 않도록 주의하세요.
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

import csv
import pymysql

# Connect to SQL Server
connect = pymysql.connect(host='Server Address', port=0, user='User ID', password='User PW', db='Schema Name', charset='charcter set')
curs = connect.cursor()
connect.commit()

print("Server Connected")

# Read CSV File
f = open("File Directory", 'r', encoding='UTF-8')
csvReader = csv.reader(f)

print("CSV File Opened")
print("----------")
print("Start Inserting Data")

count = 0

for row in csvReader:
    # Check the number of rows inserted
    count += 1
    if count == 1:
        print(count, "th row inserted")
    elif count % 1000 == 0:
        print(count, "th row inserted")

    # Data split by column
    # Variable name = (row[column number])
    # Example: accident_num = (row[1])
    num_index = (row[0]) # Index
    accident_num = (row[1]) # 사고번호
    accident_date = (row[2]) # 사고일시
    weekday = (row[3]) # 요일
    
    # SQL Qeury Example
    # INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
    sql = """INSERT INTO taas_all_data (num_index, accident_num, accident_date, weekday) values (%s, %s, %s, %s)"""
    curs.execute(sql, (num_index, accident_num, accident_date, weekday))
    
print("Finish Inserting Data")
print("----------")

# Close CSV File and SQL Server
connect.commit()
f.close()
connect.close()

print("Server Disconnected")
print("----------")
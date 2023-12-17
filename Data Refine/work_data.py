from func_data_export import data_merge_sort

import os
import chardet
import platform
import pandas as pd

system = platform.system()
encoding = "euc-kr" if system == "Windows" else "UTF-8"             # Windows = euc-kr, macOS = UTF-8

data_2007 = pd.read_csv('./Data/TAAS/csv/taas(2007-2009).csv', encoding="euc-kr")
data_2007.drop(columns=["부상신고자수", "기상상태"], inplace=True)

data_2010 = pd.read_csv('./Data/TAAS/csv/taas(2010-2012).csv', encoding="euc-kr")
data_2010.drop(columns=["부상신고자수", "기상상태"], inplace=True)

data_2013 = pd.read_csv('./Data/TAAS/csv/taas(2013-2015).csv', encoding="euc-kr")
data_2013.drop(columns=["부상신고자수", "기상상태"], inplace=True)

data_2016 = pd.read_csv('./Data/TAAS/csv/taas(2016-2018).csv', encoding="euc-kr")
data_2016.drop(columns=["부상신고자수", "기상상태"], inplace=True)
  
data_2019 = pd.read_csv('./Data/TAAS/csv/taas(2019-2021).csv', encoding="euc-kr")
data_2019.drop(columns=["부상신고자수", "기상상태"], inplace=True)

data_2022 = pd.read_csv('./Data/TAAS/csv/taas(2022).csv', encoding="euc-kr")
data_2022.drop(columns=["부상신고자수", "기상상태"], inplace=True)

print("Check Data Shape")
print(data_2007.shape)
print(data_2010.shape)
print(data_2013.shape)
print(data_2016.shape)
print(data_2019.shape)
print(data_2022.shape)
print("----------")

data_merge_sort(data_2007, "data_2007-2009")
data_merge_sort(data_2010, "data_2010-2012")
data_merge_sort(data_2013, "data_2013-2015")
data_merge_sort(data_2016, "data_2016-2018")
data_merge_sort(data_2019, "data_2019-2021")
data_merge_sort(data_2022, "data_2022")
print("----------")

# Data Merge
directory = "./Data/TAAS/after_merge_damage_violent/"
directory_list = os.listdir('./Data/TAAS/after_merge_damage_violent/')

df_CONCAT = pd.DataFrame()

for file in directory_list:
    with open(directory + file, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(10000))
        print(result)
    df = pd.read_csv(directory + file, encoding_errors='ignore')
    df_CONCAT = pd.concat([df_CONCAT, df], ignore_index=True)

df_all_SORT_VALUES = df_CONCAT.sort_values(by='사고번호', ascending=True)
print(df_all_SORT_VALUES)

print("MERGE COMPLETE")
df_all_SORT_VALUES.to_csv(path_or_buf=directory + "all_data" + ".csv")
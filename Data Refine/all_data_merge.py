import pandas as pd

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

data_list = [data_2007, data_2010, data_2013, data_2016, data_2019, data_2022]

df_CONCAT = pd.DataFrame()
directory = "./Data/TAAS/"

for index in data_list:
  df_CONCAT = pd.concat([df_CONCAT, index], ignore_index=True)

df_all_SORT_VALUES = df_CONCAT.sort_values(by='사고번호', ascending=True)

df_all_SORT_VALUES.to_csv(path_or_buf=directory + "all_data" + ".csv")

print("MERGE COMPLETE")
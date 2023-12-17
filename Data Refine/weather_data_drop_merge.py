import pandas as pd

data_2007 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2007.csv', encoding="euc-kr")
print(data_2007.shape)
data_2007.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2008 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2008.csv', encoding="euc-kr")
print(data_2008.shape)
data_2008.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2009 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2009.csv', encoding="euc-kr")
print(data_2009.shape)
data_2009.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2010 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2010.csv', encoding="euc-kr")
print(data_2010.shape)
data_2010.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2011 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2011.csv', encoding="euc-kr")
print(data_2011.shape)
data_2011.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2012 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2012.csv', encoding="euc-kr")
print(data_2012.shape)
data_2012.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2013 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2013.csv', encoding="euc-kr")
print(data_2013.shape)
data_2013.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2014 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2014.csv', encoding="euc-kr")
print(data_2014.shape)
data_2014.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2015 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2015.csv', encoding="euc-kr")
print(data_2015.shape)
data_2015.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2016 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2016.csv', encoding="euc-kr")
print(data_2016.shape)
data_2016.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2017 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2017.csv', encoding="euc-kr")
print(data_2017.shape)
data_2017.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2018 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2018.csv', encoding="euc-kr")
print(data_2018.shape)
data_2018.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2019 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2019.csv', encoding="euc-kr")
print(data_2019.shape)
data_2019.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2020 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2020.csv', encoding="euc-kr")
print(data_2020.shape)
data_2020.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2021 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2021.csv', encoding="euc-kr")
print(data_2021.shape)
data_2021.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

data_2022 = pd.read_csv('./Data/weather/OBS_ASOS_TIM_2022.csv', encoding="euc-kr")
print(data_2022.shape)
data_2022.drop(columns=["지점", "기온 QC플래그", "강수량 QC플래그", "풍속 QC플래그", "풍향 QC플래그", "습도 QC플래그", "현지기압 QC플래그", "해면기압(hPa)", "해면기압 QC플래그", "일조 QC플래그", "일사 QC플래그", "3시간신적설(cm)", "지면상태(지면상태코드)", "현상번호(국내식)", "지면온도 QC플래그"], inplace=True)

print("")
print("-----------------------")
print("")

print(data_2007.shape)
print(data_2008.shape)
print(data_2009.shape)
print(data_2010.shape)
print(data_2011.shape)
print(data_2012.shape)
print(data_2013.shape)
print(data_2014.shape)
print(data_2015.shape)
print(data_2016.shape)
print(data_2017.shape)
print(data_2018.shape)
print(data_2019.shape)
print(data_2020.shape)
print(data_2021.shape)
print(data_2022.shape)

data_list = [data_2007, data_2008, data_2009, data_2010, data_2011, data_2012, data_2013, data_2014, data_2015, data_2016, data_2017, data_2018, data_2019, data_2020, data_2021, data_2022]

df_CONCAT = pd.DataFrame()
directory = "./Data/weather/after/"

for index in data_list:
  df_CONCAT = pd.concat([df_CONCAT, index], ignore_index=True)

df_all_SORT_VALUES = df_CONCAT.sort_values(by='일시', ascending=True)

print(df_all_SORT_VALUES.shape)
print("-----------------------")
print(df_all_SORT_VALUES)

print(df_all_SORT_VALUES.loc[40])

df_all_SORT_VALUES.to_csv(path_or_buf=directory + "all_data" + ".csv")

print("MERGE COMPLETE")
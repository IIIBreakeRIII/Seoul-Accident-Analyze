# Seoul Accident Analyze

__2007년부터 2022년 서울시 교통사고 관련 데이터 분석__

---

### $Abstract$
2007년부터 2022년까지 서울시 내의 교통사고 및 조건부 교통사고를 바탕으로 하는 데이터 분석.  
교통사고 자체 데이터를 기반으로 1차적인 데이터를 분석하고, 해당 기간동안 날씨 데이터를 2차적으로 분석하여 날씨와 교통사고 간의 연관성을 찾기 위함

---

### $Contents$
- Data
  - TAAS(Traffic Accident Analysis System)
    - 도로교통공단의 교통사고분석시스템을 통해 제공하는 국내 교통사고 관련 데이터
  - 기상청에서 제공하는 날씨 데이터
- System Configure
  - __Python__ : ver.3.7.5
  - __Environment__ : Anaconda (miniforge)
  - __Matplotlib__ : ver.3.5.3
  - __Pandas__ : 1.3.5
  - __Numpy__ : 1.20.3
  - __Pymysql__ : 1.1.0
- File Description
  - [_Accident-Analyze_](https://github.com/IIIBreakeRIII/Seoul-Accident-Analyze/tree/main/Accident-Analyze) : 교통사고 데이터 분석
  - [_Data Refine_](https://github.com/IIIBreakeRIII/Seoul-Accident-Analyze/tree/main/Data%20Refine) : 데이터 가공
  - [_Guide Code_](https://github.com/IIIBreakeRIII/Seoul-Accident-Analyze/tree/main/Guide%20Code) : 서버 접근 관련 가이드
  - [_Weather-Analyze_](https://github.com/IIIBreakeRIII/Seoul-Accident-Analyze/tree/main/Weather-Analyze) : 교통사고와 날씨 사이의 연관성을 이용한 데이터 분석
  - [_Result_](https://github.com/IIIBreakeRIII/Seoul-Accident-Analyze/tree/main/Result) : 결과 그래프 도출 이미지
- Data Manage
  - 개인 서버 및 MySQL을 이용하여 데이터베이스 구축
  - 해당 데이터베이스에 관련 데이터를 Import 진행 후 서버를 이용한 데이터 분석 진행

---

### $Result$
[_Result_](https://github.com/IIIBreakeRIII/Seoul-Accident-Analyze/tree/main/Result) 참고

---

### $Contributors$
- [*__Beom__*](https://github.com/BeomKung)
- [*__Soyun__*](https://github.com/nuyos)

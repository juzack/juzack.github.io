# Pandas: 파이썬에서 데이터 분석(Data Analysis)을 할 때 가장 널리 쓰이는 라이브러리
# 표(테이블) 형태의 데이터를 다루기 위한 파이썬 라이브러리

# 이름은 "Panel Data"에서 유래
# 데이터 분석을 위한 엑셀처럼 행과 열이 있는 구조(DataFrame) 제공
# Numpy 기반으로 만들어져 빠르고 효율적이며, CSV, Excel, SQL, JSON 등 다양한 파일 형식 입출력 지원

# pip install pandas
# import pandas as pd  ## pandas 패키지를 pd라는 이름으로 사용 - alise


import pandas as pd
import numpy as np

print(pd.__version__) #판다스 버전 출력
print(np.__version__) #넘파이 버전 출력
#############################################################
#판다스의 핵심 구조(두 가지 객체): 시리즈(Series)의 데이터프레임(Dataframe)

## 1. Series
# - 1차원 데이터 (열 하나)
# - 인덱스(index) 사용 가능
# - 데이터 타입을 가진(dtype)
# 
## 2. 데이터프레임(Dataframe) :  2차원 표 형태 데이터 (행+열)

#############################
## series 생성
#############################
lista = [10, 20, 30] #리스트를 시리즈로 변환하여 변수 sr1에 저장
sr1 = pd.Series(lista) #판다스 Series() 함수로 리스트를 시리즈로 변환
sr2 = pd.Series([10, 20, 30])
print(sr1) #Series 객체 출력
print(sr2) #Series 객체 출력

sr = pd.Series(lista, dtype = float) #dtype 옵션으로데이터 타입 지정
print(sr)
input()

## numpy array로 생성
arr = np.arange(1, 10) ## 1부터 9까지의함수를 갖는 numpy array 생성
print(arr) ## numpy array 출력, [1 2 3 4 5 6 7 8 9]
sr= pd.Series(arr)
print(sr)

## dtype을 지정하여 생성한 경우
sr = pd.Series(arr,dtype=float)
print(sr)
print('1' + '=' *100)
input()

#######################################################
# - list로 생성한 경우
list_data = ['2021-01-02', 3.14, 'ABC', 100, True]   #리스트를 시리즈로변환하여 변수 sr에 저장
sr = pd.Series(list_data)
print(sr)
print('\n')
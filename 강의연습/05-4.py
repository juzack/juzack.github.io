# '''예외 처리
# 구문 오류, 존재하지 않는 파일사용 시도 - fileNotfoundError, 0으로숫자를 나누는 경우-ZeroDivisionError, IndexError
# 1. 에러 방지및 예외 처리 - 비정상 종료 방지
# 2. 사용자 경험 개선 - 오류 메시지 또는 다음 행동 안내
# 3. 코드 가독성 향상 - 오류 처리 코드와 본문 코드 분리로 try블록-필요 코드, except블록-예외 상황 처리 / 코드 가독성 높임
# 4. 정확한 예외 처리 - 특정 예외 처리 또는 다수의 예외세분화하여 다른 방식으로처리

# ValueError
# 데이터의 타입은 맞지만 그 값이 적젉하지 않을 때 발생하는 예외
# int 변환 오류 - int("hello")
# 리스트의 특정 메소드 사용 - numbers = [1, 2, 3] / numbers.remove(4)
# 잘못된 형식의 날짜 변환

# try-except
# try 블록 수행 중오류가발생하면 except블록 수행
# try 블록에서 오류가발생하지 않으면 except 블록 미수행
# ---
# try:
#    ...
# except [발생_오류 [as 오류_변수]]:
# 오류 발생했을 때 except 문에 미리 정해 놓은 ㅇ류와 동일할 때만 except 블록 수행'''

# # try:
# #     4/0
# # except ZeroDivisionError as e:
# #     print(e)    

# '''
# try-finally 문
# finally 절은 try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행
# 보통 사용한 리소스를 close해야 할 때 많이 사용-foo.txt파일을 쓰기 모드로 열어 try문을 수행한후예외 발생 여부와 상관없이 finally문으로 닫을 수 있음

# 여러 개의 오류 처리
# try
# except ZeroDivisionError as e:
# except IndexError as e: 등 / 아래와 같이 가능
# except (ZeroDivisionError, IndexError) as e:

# try-else 문
# 오류가 없을 경우에만 수행
# try:
#     ...
# except:
#     ...
# else:
#     ...

# try:
#     age = int(input('나이"))
# except:
#     print('입력')
# else:
#     if age <= 10
    
# 오류 회피 - 특정 오류발생할 경우통과 
# except:
#     pass
    
# 오류 일부러 발생
# raise 명령서 사용 오류강제 발생
#     class Bird:
#         def fly(self):
#             raise NotImplementedError
# 파이썬 내장 오류 NotImplementedError와 raise 문 활용
# fly 함수를 구현하지 않은 상태로 fly 함수호출 시 NotImplementedError 오류 발생
# class Eagle(Bird):
#     pass
    
# eagle = Eagle()
# eagle.fly()

# 예외 만들기
#     파이썬 내장 클래스인 Exception 클래스를 상속하여 생성 가능
#     class MyError(Exception):
#         pass

#     별명 출력 함수에서MyError 사용
#         def say_nick(nick):
#             if nick == '바보':
#                 raise MyError()
#             print(nick)
# '''

# # class MyError(Exception):
# #      pass

# # def say_nick(nick):
# #     if nick == '바보':
# #         raise MyError()
# #     print(nick)

# # say_nick("천사")
# # say_nick("바보")

# class MyError(Exception):
#      pass

# def say_nick(nick):
#     if nick == '바보':
#         raise MyError()
#     print(nick)

# try:
#     say_nick("천사")
#     say_nick("바보")
# except MyError:
#     print("허용되지 않는 별명입니다.")
    
'''
내장 함수: 파이썬 설치 시에 자동으로 설치되어 import 필요없이 실행할수 있는 함수
any(x) x 요소 중 하나라도 참이면 True, 모두 거짓 False
chr(i)
dir(x) 객체 변수나 함수를 보여주는 함수
divmod(a, b) a를 b로 나눈 몫과 나머지를 튜플로 리턴
enumerate(x) 열거, 순서가 있는 데이터(리스트, 튜플, 문자열)을 입력받아 인덱스 값을 포함하는enumerate 객체 리턴
eval(expression) 문자열로 구성된 표현식(expression)을 입력으로 받아 해당 문자열을 실행한 결과값을 리턴
hex(x) 정수 값을 16진수(hexadecimal)
id(object) 객체(object)를 입력받아 고유 주솟값(레퍼런스)을 리턴
isinstance(object, class) 첫 인수 객체, 두 번째 인수로 클래스 받아. 입력 받은 객체가 그 클래스의 인스턴스이닞 판단하여 참이면 True, 거짓이면 False를 리턴
len(s) 입력값 s의 길이(요소 전체 개수)를 리턴
list(iterable) 반복 가능한 데이터를 입력받아 리스트로 만들어 리턴
map(f, iterable)

max(iterable) 
miniterable)
range([start,] stop [,step])
round(number [,ndigits]) 숫자 반올림 리턴 함수, ndigits는 반올림하여 표시하고 싶은소수점 자릿수 
sorted(iterable)

str(object)
sum(iterable)
tuple(iterable)
type(object)
zip(*iterable) 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수


'''
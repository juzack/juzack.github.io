# a = input()

# number = input("Enter a number: ")
# print(f'당신이 입력한 숫자는 {number}입니다.')

# for i in range(10):
#     print(f'프린트함수{i}', end=' ')
    
# parameter 매개변수
# argument 인수

# print("A", end=', ')
# print("B", end='; ')
# print("C")
# print("D", end='\t')
# print("E", end=' ')
# print("F")

# f = open("New.txt",'w')
# # f = open("New.txt",'r')
# # f = open("New.txt",'a')

# for i in range(1, 11):
#     # data = "This is the %d line.\n" %i
#     if i<10:
#         data = f'This is the {i} line. (f-string)\n'
#     elif i==10:
#         data = f'This is the {i} line. (LastPang)'
#     f.write(data)
# f.close()

# f = open("New.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# f = open("New.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# f = open("New.txt", 'r')
# lines = f.readlines()

# print(lines)

# for line in lines:
#     print(line)
# f.close()

# f = open("New.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# f = open("New.txt", 'r')
# for line in f:
#     print(line)
# f.close()

# 반복 가능 객채(Iterable):
#  반복(for 루프 등)에서 순차적으로 요소를 하나씩 꺼낼 수 있는 객체
#  (예시) Iterable 객체들
#   - 시퀀스 타입: list, tuple, str, range
#   - 비시퀀스 컬렉션: dict(키 반복), set
#   - 파일 객체: open로 연 파일
#   - iter

# f = open("New.txt", 'a')
# for i in range(20, 30):
#     data = "\n%d line." %i
#     f.write(data)
# f.close()

# with open("New.txt", "w") as f:
#     f.write("Life is too Short")

import sys

args = sys.argv[1:]
for i in args:
    print(i)
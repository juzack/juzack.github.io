def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
    
# 내부 변수(Internal / Special Variables)
# __name__ 스크립트를 실행할 때 자동으로 부여하는 특별한 내장 변수(special built-in variable)
#          파일의 실행 맥락(Context)을 알려주는 내부 변수
#          모듈의 이름을 나타내는 변수
#          스크립트를 직접 실행하면 __main__이 되고 import되면 모듈 이름 문자열이 됨
# __file__ 현재 실행 중인 파일의 경로를 문자열로 저장
# __package__, __doc__, __dict__, __all__, __builtins__,... 
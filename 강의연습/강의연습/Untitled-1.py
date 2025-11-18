def add1(a, b):
    return a + b

def add2():
    return "Hi"

def greet1(name):
    print(f'안녕하세요, {name}님!')
    
def greet2():
    print("안녕하세요! 파이썬 함수 예제입니다.")
    
    
    
if __name__ == "__main__":
    
    result1 = add1(3, 5)
    print("결과1: ", result1)
    
    result2 = add2()
    print("결과2: ", result2)
    
    greet1("홍길동")
    
    greet2()




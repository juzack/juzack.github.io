def power1(base, exponent):
    return base ** exponent

def power2(base, exponent=2):
    return base ** exponent

def summarize1(*args):
    print("위치 인자들: ", args)
    result = 0
    for num in args:
        result += num
    return result

def summarize2(ret, *args):
    print("위치 인자들: ", args)
    result = 0
    for num in args:
        result += num
    if ret:
        return result

def summarize3(**kwargs):
    print("키워드 인자들: ", kwargs)
    
def summarize4(*args, **kwargs):
    print("위치 인자들: ", args)
    print("키워드 인자들: ", kwargs)
    
if __name__ == "__main__":
    
    print(power1(exponent=3, base=2))
    print(power1(2, 3))
    
    print(power2(3))
    print(power2(3, 3))
    
    result1 = summarize1(1, 2, 3, 4, 5)
    print(result1)
    
    result2 = summarize2(True, 1, 2, 3)
    print(result2)
    
    summarize3(name="홍길동", age=30, city="서울")
    
    summarize4(1, 2, 3, name="홍길동", age=30)
    
    
    square = lambda x:  x ** 2 ## 람다 함수 정의, 문법 -> 함수명 = lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
    print(square(4))
    
    
    numbers = [5, 2, 9, 1, 7]
    numbers.sort()
    print(numbers) # [1, 2, 5, 7, 9]
    
    ## sort()는 리스트(list) 객체가 가진 내장 메서드(함수)
    ## 기본문법: 리스트.sort(key=None, reverse=False)
    ## key -> 각 항목에서 비교 기준이 될 값을 반환하는 함수, 즉 key 인자는 정렬 기준을 지정하는 옵션(기본값)
    ## reverse -> 정렬 순서를 지정하는 옵션(기본값: False <- 오름차순)
    
    ## 람다 함수를sort() 메서드의 key 인자로 전달하여 리스트 정렬
    fruits = ["banana", "apple", "cherry", "blueberry"]
    fruits.sort(key=len) ## 각 문자열의 길이 기준으로 정렬
    print(fruits) # ['apple', 'banana', 'cherry', 'blueberry']
    
    fruits.sort(key=lambda x: len(x)) # 각 문자열의 길이 기준으로 정렬
    print(fruits) # ['apple', 'banana', 'cherry', 'blueberry']
    
    numbers = [0, -5, 3, -20, 9]
    numbers.sort(key=abs)  # 절댓값 기준 정렬
    print(numbers)  ## [3, -5, 8, 10, -20]
    
    numbers.sort(key=lambda x: abs(x))  # 절댓값 기준 정렬
    print(numbers)  ## [3, -5, 8, 10, -20]
    
    numbers.sort()  # ascending
    print(numbers)  ## 
    
    numbers.sort(reverse=True)  # descending
    print(numbers)  ## 
    
    fruits.sort(key=lambda x: x[1])  # 마지막 글자 기준으로 정렬
    print(fruits)  ## ['nanana', 'apple', 'cherry', 'blueberry'] -> a, e, y, y (ascending order)
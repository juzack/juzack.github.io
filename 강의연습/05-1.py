# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def greet(self):
#         print(f'안녕하세요, 저는 {self.name}이고 {self.age}살입니다.')
        
# p1 = Person("Tae-woong Yoo", 40)
# p1.greet()

# print(f"이름: {p1.name}")
# print(f"나이: {p1.age}")

# p1.age = 30
# p1.greet()

# 캡슐화, 상속, 구조화된 코드, 추상화, 다형성
# 1. 캡슐화 (Encapsulation) 
# 설명: 캡슐화는 데이터(속성)와 그 데이터를 조작하는 함수(메서드)를 하나의 단위(클래스)로 묶는 것을 의미합니다. 외부에서 객체의 내부 상태(데이터)에 직접 접근하는 것을 막고, 오직 클래스 내부에 정의된 메서드를 통해서만 접근하도록 하여 데이터의 무결성을 보호합니다.
# 장점: 객체의 독립성을 유지하고, 외부로부터의 부적절한 값 유입이나 조작을 방지하여 버그 발생 가능성을 줄이고 코드의 유지보수성을 향상시킵니다. 
# 목적: 
#   데이터 보호-외부 코드가 객체 내부 데이터를 임의로 수정하는 것을 방지, 
#   코드유지보수성 향상-내부 구현이 바뀌어도외부 인터페이스(메서드)는 동일하게 유지 가능
#   모듈화(Modularity)-클래스 단위로 코드 구조를 명확히분리
#   안정성(Safety)-예기치 않은 데이터 손상이나 부정확한 상태(state)를 방지
# 2. 상속 (Inheritance) 
# 설명: 상속은 이미 존재하는 클래스(부모 클래스/슈퍼 클래스)의 속성과 메서드를 새로운 클래스(자식 클래스/서브 클래스)가 물려받아 사용할 수 있도록 하는 메커니즘입니다.
# 장점: 공통 코드를 부모 클래스에 정의하고 자식 클래스에서 재사용할 수 있어 코드 중복을 최소화하고 효율성을 높입니다. 또한, 기존 코드를 변경하지 않고 기능을 추가하거나 재정의하여 확장성을 향상시킵니다. 
# 
# 3. 구조화된 코드 (Structured Code) 
# 설명: 클래스는 연관된 데이터와 기능을 논리적으로 그룹화하여 코드를 구조화하고 모듈화할 수 있게 해줍니다. 복잡한 프로그램을 더 작고 관리하기 쉬운 부분(객체)으로 나눌 수 있습니다.
# 장점: 코드 조직이 명확해지고, 각 객체는 독립적인 책임 영역을 가지므로 대규모 프로젝트에서 코드 관리와 협업이 용이해집니다. 
# 4. 추상화 (Abstraction) 
# 설명: 추상화는 객체의 공통적인 속성과 기능을 추출하여 정의하는 과정입니다. 복잡한 내부 구현은 숨기고, 사용자가 필요로 하는 핵심 기능(인터페이스)만을 노출합니다.
# 장점: 사용자는 복잡한 내부 구조를 신경 쓰지 않고도 프로그램을 사용할 수 있으며, 내부 구현이 변경되더라도 외부에 공개된 인터페이스가 유지되므로 유지보수가 용이해지고 복잡도가 감소합니다. 
# 5. 다형성 (Polymorphism) 
# 설명: 다형성은 동일한 이름의 메서드나 함수가 상황(객체의 타입)에 따라 다르게 동작하도록 하는 능력입니다. 즉, 여러 다른 클래스들이 같은 이름의 메서드를 구현할 수 있으며, 이 메서드를 호출할 때 객체의 실제 타입에 따라 적절한 구현이 실행됩니다.
# 장점: 코드를 더 유연하고 확장 가능하게 만듭니다. 새로운 클래스를 추가할 때 기존 코드를 수정할 필요 없이 일관된 방식으로 처리할 수 있습니다. 
# 이러한 객체 지향 프로그래밍(OOP)의 원칙들은 파이썬 클래스를 통해 효과적으로 구현되며, 재사용성, 유지보수성, 확장성이 뛰어난 코드를 작성할 수 있도록 돕습니다.

















# # calculator.py
# result = 0

# def add(num):
#     # global result
#     result = 0
#     result += num
#     return result

# print(add(3))
# print(add(4))

# # calculator2.py
# result1 = 0
# result2 = 0

# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))


# # calculator3.py
# class Calculator:
#     def __init__(self):
#         self.result = 0
        
#     def add(self, num):
#         self.result += num
#         return self.result
    
# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second        
    # def setdata(self, first, second):
    #     self.first = first
    #     self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# # cal1 = FourCal()
# # cal2 = FourCal()
# # cal1.setdata(4, 2)
# # cal2.setdata(3, 8)
# cal1 = FourCal(4, 2) #생성자 사용 시
# cal2 = FourCal(3, 8) #생성자 사용 시

# print(cal1.add())
# print(cal1.mul())

# print(cal2.sub())
# print(cal2.div())

# print(id(cal1))
# print(id(cal2))

# class BankAccount:
#     def __init__(self, owner, balance = 0):
#         self.owner = owner
#         self.balance = balance
#         print(f"{owner} has been updated.")

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} has been deposited. Your current balace is: {self.balance}Won")
        
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"{amount} has been withdrawn. Your remaining balance is: {self.balance}Won")
#         else:
#             print("Insufficient balace!")

#     def get_balance(self):
#         return self.balance
    
# acc = BankAccount("T1 Youu", 10000)
# acc.deposit(5000)
# acc.withdraw(12000)
# print("Current balance: ", acc.get_balance())

class moreFourCal(FourCal):
    # pass

    def pow(self):
        result = self.first ** self.second
        return result

acal1 = moreFourCal(4, 2)
print(acal1.add())
print(acal1.mul())
print(acal1.sub())
print(acal1.div())

print(acal1.pow())

# FourCal 사칙연산 되도록, 뱅크 어카운트  클라스 참고하여 숙제 제출
# 특수 메서드 예시
#__init__


# 클래스 문법


class accFourCal:
    def __init__(self, first, second, acc=0):
        self.first = first
        self.second = second        
        self.acc = acc
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
#     class FourCal:
#     def __init__(self, initial_value):
#         # 첫 번째 인수를 초기 누적 결과(result)로 설정합니다.
#         self.result = initial_value 
#         # 기존 first와 second는 누적 계산에선 필요없으므로 제거하거나 주석 처리했습니다.

#     def add(self, value):
#         # 현재 result에 value를 더하고 다시 result에 저장합니다. (누적)
#         self.result = self.result + value
#         return self.result

#     def mul(self, value):
#         # 현재 result에 value를 곱하고 다시 result에 저장합니다. (누적)
#         self.result = self.result * value
#         return self.result

#     def sub(self, value):
#         # 현재 result에서 value를 빼고 다시 result에 저장합니다. (누적)
#         self.result = self.result - value
#         return self.result

#     def div(self, value):
#         # 현재 result를 value로 나누고 다시 result에 저장합니다. (누적)
#         if value == 0:
#             return "Error: Cannot divide by zero"
#         self.result = self.result / value
#         return self.result

# # --- 사용 예시 ---
# a = FourCal(10) # 초기값 10으로 설정
# print(f"초기값: {a.result}") # 출력: 초기값: 10

# a.add(5) # 10 + 5 = 15
# print(f"5 더한 후: {a.result}") # 출력: 5 더한 후: 15

# a.mul(3) # 15 * 3 = 45
# print(f"3 곱한 후: {a.result}") # 출력: 3 곱한 후: 45

# a.sub(10) # 45 - 10 = 35
# print(f"10 뺀 후: {a.result}") # 출력: 10 뺀 후: 35

# a.div(7) # 35 / 7 = 5.0
# print(f"7로 나눈 후: {a.result}") # 출력: 7로 나눈 후: 5.0
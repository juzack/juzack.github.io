# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        
#     def info(self):
#         return f"{self.name} - {self.price}원"

# class CartItem:
#     def __init__(self, item, quantity: int = 1):
#         self.item = item
#         self.quantity = quantity
        
#     def get_total_price(self):
#         return self.item.price*self.quantity
    
#     def info(self):
#         return f"{self.item.name} x {self.quantity}개 = {self.get_total_price()}원"

# class Cart:
#     def __init__(self):
#         self.items: Dict[str, CartItem] = {}
        
#     def add_item(self, item, quantity=1):
#         if item.name in self.items:
#             self.items[item.name].quantity += quantity
#         else:
#             self.items[item.name] = CartItem(item, quantity)
#         print(f"[장바구니] {item.name}의 수량이 {quantity}만큼 증가 (현재 수량: {self.items[item.name].quantity})")

#     def remove_item(self, item_name):
#         if item_name in self.items:
#             del self.items[item_name]
#             print(f"[장바구니] {item_name} 삭제완료")
#         else:
#             print("[장바구니] 해당 상품이 없습니다.")
#             return

#     def change_quantity(self, item_name, quantity):
#         if item_name in self.items:
#             if quantity <= 0:
#                 self.remove_item(item_name)
#                 print(f"[알림] '{item_name}'의 수량이 0 이하가 되어")
#         else:
#             self.items[item_name].quantity = quantity
#             print(f"[알림] '{item_name}'의 수량이 {quantity}로 변경")
        
        
#     def get_total(self):
#         total_price = 0
#         for cart_item in self.items.values():
#             total_price += cart_item.get_total_price()
#         return total_price
        
#     def is_empty(self):
#         return bool(not self.items)
    
#     def summary(self):
#         print("\n--- 장바구니 현황 ---")
#         if self.is_empty():
#             print("장바구니가 비어있음")
#         else:
#             for cart_item in self.items.values():
#                 print(f"- {cart_item.info()}")
#             print(f"---------------------")
#             print(f"총 결제 금액: {self.get_total()}원")
#         print("-------------------\n")

# class User:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.cart = Cart()
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"[충전 알림] {amount}원이 충전. 현재 잔액: {self.balance}원")
#         else:
#             print("[주의] 0원 이상의 금액을 입력해주세요.")
            
#     def show_balance(self):
#         print(f"[잔액 확인] 현재 '{self.name}'님의 잔액은 {self.balance}원")
        
#     def checkout(self):
#         total_to_pay = self.cart.get_total()
        
#         print(f"\n--- 결제 시도 ---")
#         print(f"결제할 총 금액: {total_to_pay}원")
#         print(f"현재 잔액: {self.balance}원")
        
#         if self.balance < total_to_pay:
#             print("[결제 실패] 잔액이 부족. 결제 수행 불가")
#         else:
#             self.balance -= total_to_pay
#             print("[결제 완료] 결제가 성공적으로 시행")
#             self.cart.items = {}
#             print("[알림] 장바구니가 비워짐")
#             self.show_balance()
#         print(f"--------------------\n")
        
# products = [
#     Item("노트북", 10000),
#     Item("마우스", 5000),
#     Item("키보드", 2000),
#     Item("모니터", 1000),
# ]

# username = input("사용자 이름을 입력하세요: ").strip() or "Guest"
# user = User(username, balance = 0)
# print(f"{user.name}님, 환영합니다!")

# def display_menu():
#     print("\n" + "="*20)
#     print("=== 쇼핑몰 메뉴 ===")
#     print("1. 상품 목록 보기")
#     print("2. 장바구니에 담기")
#     print("3. 장바구니 보기/수정")
#     print("4. 결제하기")
#     print("5. 잔액 충전")
#     print("6. 잔액 조회")
#     print("0. 종료")
#     print("="*20)

# def handle_add_to_cart():
#     print("\n--- 상품 목록 ---")
#     for i, item in enumerate(products, 1):
#         print(f"{i}. {item.info()}")
#     print("-------------")

#     try:
#         choice = int(input("장바구니에 담을 상품 번호를 입력 (0: 취소): "))
#         if choice == 0:
#             return
        
#         if 1 <= choice <= len(products):
#             selected_item = products[choice - 1]
#             quantity = int(input(f"'{selected_item.name}' 수량을 입력: "))
#             if quantity > 0:
#                 user.cart.add_item(selected_item, quantity)
#                 print(f"[완료] {quantity}개의 '{selected_item.name}'가 추가")
#             else:
#                 print("[경고] 수량은 1 이상이어야 합니다.")
#         else:
#             print("[경고] 유효한 숫자(정수)를 입력해주세요.")
            
# def handle_cart_management():
#     user.cart.summary()
#     if user.cart.is_empty():
#         return
    
#     action = input("수정/삭제할 항목의 번호를 입력하거나 (E: 종료): ").upper()
#     if action == 'E':
#         return
    
#     try:
#         item_index = int(action)
#         item_names = list(user.cart.items.keys())
#         if 1 <= item_index <= len(item_names):
#             item_name = item_names[item_index - 1]
#             new_quantity_str = input(f"'{item_name}'의 새 수량을 입력 (0 입력 시 삭제): ")
#             new_quantity = int(new_quantity_str)
#             user.cart.change_quantity(item_name, new_quantity)
#             user.cart.summary()
#         else:
#             print("[경고] 유효하지 않은 항목 번호")
#     except ValueError:
#         print("[경고] 유효한 숫자 또는 'E'를 입력해주세요.")
        
# def main():
#     while True:
#         display_menu()
#         choice = input("메뉴를 선택하세요: ").strip()
        
#         if choice == '1':
#             # print("\n--- 상품 목록 ---")
#             # for item in products:
#             #     print(f"- {item.info()}")
#             # print("------------------")
#         elif choice == '2':
#             print_products(products)
#             try:
#                 idx = int(input("담을 상품 번호: ").strip())
#                 qty = int(input("수량: ").strip())
#             except ValueError:
#                 print("번호와 수량은 정수여야 합니다.")
#                 continue
#             if not (1 <= idx <= len(products)):
#                 print("존재하지 않는 상품 번호입니다.")
#                 continue
#             if qty <= 0:
#                 print("수량은 1 이상이어야 합니다.")
#                 continue
#             item = products[idx - 1]
#             user.cart.add_item(item, qty)
#             # handle_add_to_cart()
#         elif choice == '3':
#             cart_menu(user)
#             # handle_cart_management()
#         elif choice == '4':
#             user.checkout()
#         elif choice== '5':
#             try:
#                 amount = int(input("충전할 금액을 입력하세요: ").strip())
#                 # user.deposit(amount)
#             except ValueError:
#                 print("[경고] 유효한 금액(정수)를 입력해주세요.")
#                 continue
#             user.deposit(amount)
#         elif choice == '6':
#             user.show_balance()
#         elif choice == '0':
#             print("쇼핑 시뮬레이터를 종료합니다.")
#             break
#         else:
#             print("[경고] 유효하지 않은 메뉴 선택입니다. 다시 시도해주세요.")
            
# if __name__ == "__main__":
#     main()
    
# # 파이썬으로 쇼핑 카트 & 결제 시뮬레이터를 구현하려고해. 여러 객체(Item, CartItem, Cart, User)를 설계하고, 메서드 호출을 통해 객체 상호작용을 구현하고자해. 
# # Item 클래스부터 구현 설계방법을 알고 싶어 - 속성: name, price - 메서드: info() 메서드 -> "사과 - 1500원"형태의 문자열을 반환하는 메서드
# # CartItem 클래스를 구현해야해. - 속성: item, quantity - 메서드: get_total_price() -> item.price*quantity 값 반환 info() -> "사과 x 3개 = 4500원" 형태의 문자열 반환
# # Cart 클래스는
# #  - 속성: items(장바구니에 담긴 상품 목록)_리스트 또는 딕셔너리 사용(예: dict[str, CartItem] 형태 등
# #  - 메서드:
# #     -- add_item(item, quantity=1): 해당 상품을 장바구니에 추가, 이미 존재하는 상품이면 수량을 증가
# #     -- remove_item(item_name): 상품 이름을 기준으로 장바구니에서 삭제
# #     -- change_quantity(item_name, quantity): 해당 상품의 수량을 quantity로 변경, quantity가 0 이하인 경우, 해당 상품을 장바구니에서 삭제
# #    -- get_total(): 장바구니에 담긴 모든 상품의 총 금액을 계산하여 반환
# #    -- is_empty(): 장바구니가 비어있는지 여부 반환
# #    -- summary(): 장바구니 목록 및 각 상품의 금액, 총 금액을 콘솔에 출력
# # User 클래스는
# #  - 속성: name(사용자 이름), balance(보유 잔액), cart(Cart 객체(해당 사용자의 장바구니))
# #  - 메서드:
# #      -- deposit(amount) : anount만큼 잔액 충전
# #      -- show_balance(): 현재 잔액을 콘솔에 출력
# #      -- checkout(): 
# #          --- total = cart.get_total()로 장바구니 총 금액을 계산
# #          --- 만약 balance < total이면  -> "잔액 부족, 결제 실패" 메시지를 출력하고 결제를 수행하지 않는다.TimeoutError
# #          --- 충분한 잔액이 있을 경우 -> balance에서 total 만큰 차감하고, -> 결제 완료 메시지를 출력한 뒤, -> 장바구니를 비운다.
# # [추가 요구사항: 콘솔 메뉴]
# # 프로그램 실행 시 다음과 같은 메뉴를 반복해서 출력하고, 사용자의 입력에 따라 해당 기능을 수행하도록 main 루프를 작성하시오.
# # ===쇼핑몰 메뉴=====
# # 1. 상품 목록 보기
# # 2. 장바구니에 담기
# # 3. 장바구니 보기/수정
# # 4. 결제하기
# # 5. 잔액 충전
# # 6. 잔액 조회
# # 0. 종료
# # ==================

from typing import Dict, List, Optional

# =====================================================================
# 1단계: 클래스 정의 (Item, CartItem, Cart, User)
# =====================================================================

class Item:
    """상품(Item) 정보를 나타내는 클래스"""
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def info(self) -> str:
        """'상품명 - 가격원' 형태의 문자열을 반환"""
        return f"{self.name} - {self.price}원"

class CartItem:
    """장바구니에 담긴 특정 상품(Item)의 정보(수량 포함)를 나타내는 클래스"""
    def __init__(self, item: Item, quantity: int):
        self.item = item
        self.quantity = quantity

    def get_total_price(self) -> int:
        """현재 CartItem의 총 가격 (상품 가격 * 수량)을 계산하여 반환"""
        return self.item.price * self.quantity

    def info(self) -> str:
        """'상품명 x 수량개 = 총가격원' 형태의 문자열을 반환"""
        return f"{self.item.name} x {self.quantity}개 = {self.get_total_price()}원"

class Cart:
    """장바구니 역할을 하는 클래스"""
    def __init__(self):
        # key: 상품 이름 (str), value: CartItem 객체
        self.items: Dict[str, CartItem] = {}

    def add_item(self, item: Item, quantity: int = 1):
        """상품을 장바구니에 추가하거나 수량을 증가시킵니다."""
        if item.name in self.items:
            self.items[item.name].quantity += quantity
            print(f"[알림] '{item.name}' 수량 {quantity} 증가 (현재: {self.items[item.name].quantity}개)")
        else:
            cart_item = CartItem(item, quantity)
            self.items[item.name] = cart_item
            print(f"[알림] '{item.name}' {quantity}개 장바구니 추가 완료")

    def remove_item(self, item_name: str):
        """상품 이름을 기준으로 장바구니에서 상품을 삭제합니다."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"[알림] '{item_name}'이(가) 장바구니에서 삭제되었습니다.")
        else:
            print(f"[경고] '{item_name}'은(는) 장바구니에 존재하지 않습니다.")

    def change_quantity(self, item_name: str, quantity: int):
        """해당 상품의 수량을 변경합니다. 수량이 0 이하면 삭제합니다."""
        if item_name in self.items:
            if quantity <= 0:
                self.remove_item(item_name) # del 없이 메서드 호출
            else:
                self.items[item_name].quantity = quantity
                print(f"[알림] '{item_name}' 수량 {quantity}로 변경 완료")
        else:
            print(f"[경고] '{item_name}'은(는) 장바구니에 존재하지 않습니다.")

    def get_total(self) -> int:
        """장바구니에 담긴 모든 상품의 총 금액을 계산하여 반환"""
        return sum(item.get_total_price() for item in self.items.values())

    def is_empty(self) -> bool:
        """장바구니가 비어있는지 여부 반환"""
        return not self.items

    def summary(self):
        """장바구니 목록 및 총 금액을 콘솔에 출력"""
        print("\n--- 장바구니 현황 ---")
        if self.is_empty():
            print("장바구니가 비어 있습니다.")
        else:
            for i, cart_item in enumerate(self.items.values(), 1):
                print(f"{i}. {cart_item.info()}")
            print(f"---------------------")
            print(f"총 결제 금액: {self.get_total()}원")
        print("---------------------\n")

class User:
    """사용자 정보(이름, 잔액, 장바구니)를 관리하고 결제를 처리하는 클래스"""
    def __init__(self, name: str, balance: int = 0):
        self.name = name
        self.balance = balance
        self.cart = Cart() # User는 Cart 객체를 소유

    def deposit(self, amount: int):
        """amount만큼 잔액을 충전"""
        if amount > 0:
            self.balance += amount
            print(f"[충전 알림] {amount}원 충전 완료. 현재 잔액: {self.balance}원")
        else:
            print("[경고] 0원 이상의 금액을 입력해주세요.")

    def show_balance(self):
        """현재 잔액을 콘솔에 출력"""
        print(f"[잔액 확인] 현재 '{self.name}'님의 잔액은 {self.balance}원입니다.")

    def checkout(self):
        """장바구니 총 금액을 계산하고, 잔액이 충분하면 결제를 진행"""
        total_to_pay = self.cart.get_total()
        print(f"\n--- 결제 시도 (총 {total_to_pay}원) ---")

        if self.balance < total_to_pay:
            print("[결제 실패] 잔액이 부족합니다.")
        else:
            self.balance -= total_to_pay
            print("[결제 완료] 결제가 성공적으로 이루어졌습니다.")
            self.cart.items = {} # 장바구니 비우기
            self.show_balance()
        print(f"-------------------\n")

# =====================================================================
# 2단계: 메인 루프 (콘솔 메뉴 시스템)
# =====================================================================

# 판매할 상품 목록 초기화
products: List[Item] = [
    Item("사과", 100),
    Item("딸기", 50),
    Item("바나나", 80),
    Item("망고", 200),
]

# 사용자 계정 생성 및 초기 잔액 설정
# user = User("사용자", balance=0)
username = input("사용자 이름을 입력하세요: ").strip() or "Guest"
user = User(username, balance = 0)
print(f"{user.name}님, 환영합니다!")


def display_menu():
    """메뉴를 출력하는 함수"""
    print("\n" + "="*20)
    print("=== 쇼핑몰 메뉴 ===")
    print("1. 상품 목록 보기")
    print("2. 장바구니에 담기")
    print("3. 장바구니 보기/수정")
    print("4. 결제하기")
    print("5. 잔액 충전")
    print("6. 잔액 조회")
    print("0. 종료")
    print("="*20)

def handle_add_to_cart():
    """상품을 장바구니에 추가하는 사용자 입력 처리"""
    print("\n--- 상품 목록 ---")
    for i, item in enumerate(products, 1):
        print(f"{i}. {item.info()}")
    print("---------------")

    try:
        choice = int(input("장바구니에 담을 상품 번호를 입력하세요 (0: 취소): "))
        if choice == 0:
            return
        
        if 1 <= choice <= len(products):
            selected_item = products[choice - 1]
            quantity = int(input(f"'{selected_item.name}' 수량을 입력하세요: "))
            if quantity > 0:
                user.cart.add_item(selected_item, quantity)
            else:
                print("[경고] 수량은 1 이상이어야 합니다.")
        else:
            print("[경고] 유효하지 않은 상품 번호입니다.")
    except ValueError:
        print("[경고] 유효한 숫자(정수)를 입력해주세요.")

def main():
    """프로그램의 메인 실행 루프"""
    while True:
        display_menu()
        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            print("\n--- 상품 목록 ---")
            for item in products:
                print(f"- {item.info()}")
            print("---------------")
        elif choice == '2':
            handle_add_to_cart()
        elif choice == '3':
            user.cart.summary()
        elif choice == '4':
            user.checkout()
        elif choice == '5':
            try:
                amount = int(input("충전할 금액을 입력하세요: "))
                user.deposit(amount)
            except ValueError:
                print("[경고] 유효한 금액(정수)을 입력해주세요.")
        elif choice == '6':
            user.show_balance()
        elif choice == '0':
            print("쇼핑 시뮬레이터를 종료합니다.")
            break
        else:
            print("[경고] 유효하지 않은 메뉴 선택입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    # 프로그램 시작 시 main 함수 실행
    main()

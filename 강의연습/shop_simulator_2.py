class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"{self.name} - {self.price}원"

class CartItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def get_total_price(self):
        return self.item.price * self.quantity

    def info(self):
        return f"{self.item.name} x {self.quantity}개 = {self.get_total_price()}원"

class Cart:
    def __init__(self):
        self.items: dict[str, CartItem] = {}

    def add_item(self, item, quantity = 1):
        if item.name in self.items:
            self.items[item.name].quantity += quantity
            print(f"[알림] '{item.name}' 수량 {quantity} 증가 (현재: {self.items[item.name].quantity}개)")
        else:
            cart_item = CartItem(item, quantity)
            self.items[item.name] = cart_item
            print(f"[알림] '{item.name}' {quantity}개 장바구니 추가 완료")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"[알림] '{item_name}'이(가) 장바구니에서 삭제되었습니다.")
        else:
            print(f"[경고] '{item_name}'은(는) 장바구니에 존재하지 않습니다.")

    def change_quantity(self, item_name, quantity):
        if item_name in self.items:
            if quantity <= 0:
                self.remove_item(item_name)
            else:
                self.items[item_name].quantity = quantity
                print(f"[알림] '{item_name}' 수량 {quantity}로 변경 완료")
        else:
            print(f"[경고] '{item_name}'은(는) 장바구니에 존재하지 않습니다.")

    def get_total(self):
        return sum(item.get_total_price() for item in self.items.values())

    def is_empty(self):
        return not self.items

    def summary(self):
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
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.cart = Cart() 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"[충전 알림] {amount}원 충전 완료. 현재 잔액: {self.balance}원")
        else:
            print("[경고] 0원 이상의 금액을 입력해주세요.")

    def show_balance(self):
        print(f"[잔액 확인] 현재 '{self.name}'님의 잔액은 {self.balance}원입니다.")

    def checkout(self):
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

products: list[Item] = [
    Item("사과", 100),
    Item("딸기", 50),
    Item("바나나", 80),
    Item("망고", 200),
]

username = input("사용자 이름을 입력하세요: ").strip() or "Guest"
user = User(username, balance = 0)
print(f"{user.name}님, 환영합니다!")


def display_menu():
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
        
def handle_cart_management():
    while True:
        user.cart.summary()
        if user.cart.is_empty():
            return
        
        action = input("수정/삭제할 항목의 번호를 입력하거나 (E: 종료): ").upper()
        if action == 'E':
            return
        
        try:
            item_index = int(action)
            item_names = list(user.cart.items.keys())
            if 1 <= item_index <= len(item_names):
                item_name = item_names[item_index - 1]
                new_quantity_str = input(f"'{item_name}'의 새 수량을 입력 (0 입력 시 삭제): ")
                new_quantity = int(new_quantity_str)
                user.cart.change_quantity(item_name, new_quantity)
                user.cart.summary()
                break
            else:
                print("[경고] 유효하지 않은 항목 번호")
                continue
        except ValueError:
            print("[경고] 유효한 숫자 또는 'E'를 입력해주세요.")
            continue

def main():
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
            handle_cart_management()
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
    main()

from decimal import Decimal     #데이터형을 불러주기 위해 import



class Product:      # Product 클래스 생성
    def __init__(self, name, price):    # 클래스 초기화
        self.name = name
        self.price = Decimal(price)

    def get_name(self):     # Product의 이름을 불러오기 위한 메서드 생성
        return self.name

    def get_price(self):    # Product의 가격을 불러오기 위한 메서드 생성
        return self.price

class Order:        # Order 클래스 생성
    def __init__(self, products=None, total=0):
        if products is None:    # 초기값에 리스트를 불러 올 수도 있게 생성, 디폴트는 빈 리스트로 생성
            products = []
        self.products = products
        self.total = total

    def add_item(self, product: Product):
        """
        for e in self.products:
            if name == e.get_name():        # 중복을 신경 쓸 경우 추가
                return
        """
        self.products.append(product)   # 중복은 신경 쓰지 않고 추가
        self.total += product.price

    def calculate_final_price(self,tax_rate: Decimal): # 세후 금액 계산하는 메서드
        return round(((1+tax_rate) * self.total),2)

    def get_item(self,name: str):   # 문자열을 입력받아 문자열과 이름이 똑같은 Product 객체를 불러오는 매서드
        for e in self.products:     # 객채들을 하나씩 확인
            if name == e.get_name():    # 입력받은 문자열과 이름이 같은게 있는지 확인
                return e            # 있으면 반환
            return None             # 반복문이 끝났다면 없다는 것이므로 None 반환

    def remove_item(self, name: str):   #문자열을 입력받아 문자열과 이름이 똑같은 Product 객체를 삭제하는 매서드
        for e in self.products:         # 객채들을 하나씩 확인
            if name == e.get_name():    # 입력받은 문자열과 이름이 같은게 있는지 확인
                rm_price = e.get_price()    # 뺄 금액을 변수지정
                self.total -= Decimal(rm_price) # 금액을 뺌
                self.products.remove(e)     #  항목을 삭제
                return True
        return False



# test
"""

if __name__ == "__main__":
    # Order 객체 생성
    my_order = Order()

    # Product 객체 추가
    my_order.add_item(Product("Apples", "3.16"))
    my_order.add_item(Product("Bananas", "1.06"))

    # 최종 가격 계산 (판매세 6% 적용)
    final_price = my_order.calculate_final_price(Decimal(0.06))

    # 최종 가격 출력
    print(f"최종 가격 (세금 포함): {final_price}")  # 예상 출력: 4.47


"""

new_order = Order() # 객체 지정


while True:     #주문관리 시스템 반복문 시작
    sel = int(input("""
===========================================
             주문 관리 시스템             
=========================================== 

 [1] 제품 추가           [2] 제품 제거
 [3] 제품 목록 보기      [4] 제품 상세 보기
 [5] 최종 가격 계산      [6] 프로그램 종료
"""))           #UI
    if sel == 6: break  #프로그램 종료

    if sel == 1:    # 이름과 가격을 각각 입력시켜 새 제품 들여오는 코드
        product_name = input("제품 명을 입력 하시오 : ")
        product_price = input("제품의 가격을 입력 하시오 : ")
        new_order.add_item(Product(product_name, product_price))

    elif sel == 2:  # 이름을 입력시켜 제품을 제거하는 코드 있으면 삭제확인 메세지를 띄움, 없으면 존재하지 않음을 표현
        product_name = input("제거할 제품 명을 입력 하시오 : ")
        torf = new_order.remove_item(product_name)
        if torf:
            print(f"{product_name}을 삭제하였습니다.")
        else:
            print("존재하지 않는 상품입니다.")

    elif sel == 3:  # 모든 제품을 보여주는 코드
        for e in new_order.products:
            print(f"{e.get_name():10} | {e.get_price():8}$")


    elif sel == 4:  # 이름을 받아 해당하는 제품을 보여주는 코드
        product_name = input("확인할 제품 명을 입력 하시오 : ")
        sel_product = new_order.get_item(product_name)
        if sel_product is None: #없는것을 명시
            print("해당하는 상품이 없습니다.")
        else:   #있으면 이를 보여줌
            print(f"{sel_product.get_name:10} | {sel_product.get_price:8}$")

    elif sel == 5: # 세후 가격을 보여주는 코드
        final_price = new_order.calculate_final_price(Decimal(0.06))
        print(f"최종 가격 (세금 포함): {final_price}")
    while True: # 결과를 띄워놓기 위해 생성한 반복문
        keep_going = int(input("[1]메뉴로 돌아가기"))
        if keep_going == 1: break


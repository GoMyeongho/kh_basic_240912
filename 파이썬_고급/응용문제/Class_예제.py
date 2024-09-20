from decimal import Decimal



class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = Decimal(price)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Order:
    def __init__(self, products=None, total=0):
        if products is None:
            products = []
        self.products = products
        self.total = total

    def add_item(self, product: Product):
        self.products.append(product)
        self.total += product.price

    def calculate_final_price(self,tax_rate: Decimal):
        return round(((1+tax_rate) * self.total),2)

    def get_item(self,name: str):
        for e in self.products:
            if name == e.get_name():
                return e
            return None

    def remove_item(self, name: str):
        for e in self.products:
            if name == e.get_name():
                rm_price = e.get_price()
                self.total -= Decimal(rm_price)
                self.products.remove(e)
                return True
        return False



# test
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

new_order = Order()


while True:
    sel = int(input("""
===========================================
             주문 관리 시스템             
=========================================== 

 [1] 제품 추가           [2] 제품 제거
 [3] 제품 목록 보기      [4] 제품 상세 보기
 [5] 최종 가격 계산      [6] 프로그램 종료
"""))
    if sel == 6: break

    if sel == 1:
        product_name = input("제품 명을 입력 하시오 : ")
        product_price = input("제품의 가격을 입력 하시오 : ")
        new_order.add_item(Product(product_name, product_price))

    elif sel == 2:
        product_name = input("제거할 제품 명을 입력 하시오 : ")
        new_order.remove_item(product_name)

    elif sel == 3:
        for e in new_order.products:
            print(f"{e.get_name():10} | {e.get_price():8}$")


    elif sel == 4:
        product_name = input("확인할 제품 명을 입력 하시오 : ")
        sel_product = new_order.get_item(product_name)
        print(f"{sel_product.get_name:10} | {sel_product.get_price:8}$")

    elif sel == 5:
        final_price = new_order.calculate_final_price(Decimal(0.06))
        print(f"최종 가격 (세금 포함): {final_price}")
    while True:
        keep_going = int(input("[1]메뉴로 돌아가기"))
        if keep_going == 1: break


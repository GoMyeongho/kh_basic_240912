import decimal


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = decimal.Decimal(price)

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

    def add_item(self,product: Product):
        self.products.append(product)
        self.total += product.price

    def calculate_final_price(self,tax_rate: decimal.Decimal):
        return round(((1+tax_rate) * self.total),2)

    def get_item(self,name: str):
        if name in self.products.name:
            return name
        else:
            return None

    def remove_item(self, name: str):
        count = False
        if name in self.products:
            self.total -= self.products.price
            self.products.remove(name)
            count = True
        return count





if __name__ == "__main__":
    # Order 객체 생성
    my_order = Order()

    # Product 객체 추가
    my_order.add_item(Product("Apples", "3.16"))
    my_order.add_item(Product("Bananas", "1.06"))

    # 최종 가격 계산 (판매세 6% 적용)
    final_price = my_order.calculate_final_price(decimal.Decimal(0.06))

    # 최종 가격 출력
    print(f"최종 가격 (세금 포함): {final_price}")  # 예상 출력: 4.47




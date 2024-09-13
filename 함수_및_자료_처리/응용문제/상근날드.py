# 햄버거 가격 3개
# 음료 가격 2개
# 출력 : 세트 메뉴 가격 = 햄버거 3개 중 제일 싼거 + 음료 2개 중 싼거 - 50
# 입력 : 1000 1500 3000 1200 750
# 세트 : 1700원

price = list(map(int,input("햄버거 3개와 음료 2개의 가격을 입력하시오 : ").split()))
set_price = min(price[:3]) + min(price[3:5]) - 50
print(f"세트의 가격은 : {set_price}")

# 슬라이싱 없이 풀기

"""

min_burger = price[0]
min_drink = price[3]

for i in range(len(price)):
    if i < 3 and min_burger > price[i]:
        min_burger = price[i]
    if  2 < i and min_drink > price[i]:
        min_drink = price[i]
print(min_drink + min_burger - 50)

"""





















# 딕셔너리? 키로 값을 찾는 것
# {} 중괄호로 딕셔너리 선언
# 각 요소는 ','(쉼표)로 구분
# 키와 값은 ':'(콜론)으로 구분

coffee_menu = {"Americano" : 2500, "Espresso" : 2500, "Latte" : 4000, "Moca" : 4500}
food_menu = {"Cake" : 5000, "Bakery" : 6000}

print(coffee_menu)
print(coffee_menu["Americano"])     # 키로 값을 찾음
print(coffee_menu.get("Moca"))      # get(키)함수로 값을 가져옴


# 값 추가, 삭제, 키 존재 여부 확인
food_menu["IceCream"] = 5000        # 새로운 키와 값을 추가
del coffee_menu["Latte"]            # 해당 명령어로 아이템(키 + 값) 삭제

if "Bakery" in food_menu:
    print(f"Bakery price : {food_menu["Bakery"]}")
else: print("해당 메뉴가 없습니다.")

# update 함수 : 딕셔너리의 데이터를 한꺼번에 변경할 때 사용
coffee_menu.update({"Americano" : 2800, "Espresso" : 2800,
                    "Latte" : 4400, "Moca" : 4900})
print(coffee_menu)

# 정보 얻기 : keys(), values(), items()
dict_lang = {"Java" : 99, "JavaScript" : 80, "python" : 92 , "C++" : 89}
print(dict_lang.keys())
print(dict_lang.values())
print(dict_lang.items())







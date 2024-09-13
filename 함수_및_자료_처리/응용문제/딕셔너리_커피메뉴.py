# 커피 메뉴 만들기
# [1] 메뉴 보기  [2] 메뉴 조회  [3] 메뉴 추가  [4] 메뉴 삭제 [5] 파일 불러오기  [6] 파일 저장하기 [7] 종료하기
# 카테고리별 조회

import json

menu = {
    "Americano" : ["Coffee", 2000, "기본 커피 입니다."],
    "Espresso" : ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MilkTea": ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}
filename = "../menu.json"
# 파일에서 메뉴를 읽어 오는 함수
def load_menu():
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("해당 파일이 없습니다")
    except json.JSONDecodeError:
        print("JSON 디코딩 실패")

# 파일을 저장하는 함수
def save_menu():
    with open(filename, "w" , encoding="utf-8") as file:
        json.dump(menu, file, ensure_ascii=False, indent=4)


# [1] 메뉴 보기
def print_menu():
    # for key in menu:
    #     print(f"{key:10} : {menu[key]}")
    for key, value in menu.items():
        print(f"{key:10} : {value}")

# [2] 메뉴 조회(개별)
def get_menu(key):
    if key in menu:
        print(menu[key])
    else:
        print("찾는 메뉴가 없습니다.")

# [3] 메뉴 추가
def add_menu(key,category,price,desc):   # key, 분류, 가격, 설명
    if key not in menu:         # 해당 키에 대한 메뉴가 없음
        menu[key] = [category,price,desc]
        print(f"{key} 메뉴가 추가 되었습니다.")
    else:
        print("이미 존재하는 메뉴입니다.")

# [4] 메뉴 삭제
def del_menu(key):
    if key in menu:
        del menu[key]
        print(f"{key} 메뉴가 삭제 되었습니다.")
    else:
        print("존재하지 않는 메뉴입니다.")

# 카테고리 조회
def get_category(category):
    for key, value in menu.items():
         if category == value[0]:
             print(key, value)



while True:
    n = int(input("[1] 메뉴 보기  [2] 메뉴 조회  [3] 카테고리 조회  [4] 메뉴 추가  [5] 메뉴 삭제\n"
                  " [6] 파일 불러오기  [7] 파일 저장하기  [8] 종료 하기 \n"))
    if n == 1: print_menu()
    elif n == 2: get_menu(input("확인 하려는 메뉴의 이름을 입력 하시오 : "))
    elif n == 3: get_category(input("카테고리를 입력 하시오 :"))
    elif n == 4:
        name = input("추가하는 메뉴의 이름을 입력 하시오 : ")
        category = input("추가하는 메뉴의 종류를 입력 하시오 : ")
        price = int(input("추가하는 메뉴의 가격을 입력 하시오 : "))
        desc = input("추가하는 메뉴의 설명을 입력 하시오 : ")
        add_menu(name,category,price,desc)
    elif n == 5: del_menu(input("삭제하는 메뉴의 이름을 입력 하시오 : "))
    elif n == 6: menu = load_menu()
    elif n == 7: save_menu()
    elif n == 8:
        print("영업을 종료 합니다.")
        break
    else:
        print("잘못된 입력 입니다.")











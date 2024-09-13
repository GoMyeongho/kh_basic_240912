# 커피 메뉴 만들기
# [1] 메뉴 보기  [2] 메뉴 조회  [3] 메뉴 추가  [4] 메뉴 삭제  [5] 종료하기

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

while True:














# 함수란? 코드의 특정 블럭을 하나의 이름으로 묶는 것
# 코드의 재사용성을 높임, 가독성 향상
# 함수는 매개변수를 가질 수 있고, 반환값을 가질 수 있음
# 식별자는 스네이크 표기법으로 작성하고, 식별자 뒤에 '()'(소괄호)가 있음
# 일반적으로 매개변수와 함수의 호출하는 인자의 갯수가 일치해야 함
# def 키워드를 사용해서 정의
from patsy.user_util import balanced


# 함수의 반복호출



def name_card(name, addr, phone, position):
# 함수를 선언하고 매개변수로 4개의 값을 입력받을 수 있게
    print(f"{position} : {name}")
    print(f"전화번호 : {phone}")
    print(f"주소 : {addr}")
    print("="*30)

"""

name_card("안유진","서울시 강남구 역삼동",
          "010-1234-5678","리더")
name_card("장원영","서울시 강남구 삼성동",
          "010-1234-1234","센터")
name_card("가을","서울시 강남구 신사동",
          "010-5678-5678","싱어")

"""

# 은행 계좌 개설하기

def open_account(name):     # 매개변수도 있고, 반환값도 존재하는 함수 선언
    print(f"{name}님의 계좌를 개설 하였 습니다.")
    return name

def deposit(balance, in_val):    # 잔액과 입금을 매개변수로 전달 받음
    print(f"{in_val} 입금 되었습니다. 잔액은 {balance + in_val} 입니다.")
    return balance + in_val     # 기존 잔액에서 입금 금액을 더해서 반환

def withdraw(balance, out_val): # 잔액과 출금을 매개변수로 전달 받음
    if balance >= out_val:
        print(f"{out_val} 출금 되었습니다. 잔액은 {balance - out_val} 입니다.")
        return balance - out_val
    else:
        print(f"잔액이 부족합니다. 잔액은 {balance} 입니다.")
        return balance

balance = 0
name = input("계좌 개설할 이름을 입력하시오 : ")
open_account(name)   # 인자값으로 전달한 이름을 반환값으로 되돌려 받음
balance = deposit(balance, 1000)
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
print(f"{name} 잔액은 {balance} 입니다.")
# 외부에서 선언한 잔액을 인자값으로 전달, 입금액을 인자값으로 전달



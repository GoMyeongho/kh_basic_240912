#표준 입출력 : 콘솔 입출력을 의미
# [] 대괄호 : 리스트를 표시
# {} 중괄호 : 딕션을 표시
# () 소괄호 : 함수의 인수, 튜플
from time import sleep

# print() : 화면 출력을 위한 함수

print(36)
print("문자열")
print([1,2,3]) # 리스트 출력
print("파" + "이" + "썬", end='') # + : 문자열을 이어주는 연산
print("파","이","썬") # ,(seperator,comma) : 구분자를 의미, 구분자의 기본 값은 공백
print("파""이""썬")

# 이스케이프 문자 : 출력 구간의 흐름을 제어
# \n(줄바꿈), \t(탭을 의미), \b(백스페이스), \r(커서를 맨 앞으로 돌림)

print('\n' , sep=" ", end='\n')
print("Banana\b")
print("Banana\rApple")

year =  2024
month = 9
day  = 10


print(f"{year}",f"{month}",f"{day}",sep="-")
print(year,month,day,sep="-")

# for i in range(1, 101):
#     print(f"\r{i}%", end='')
#     sleep(0.1)

#출력 스타일 정리
name = "고명호"
age = 26
gender = "남성"
job = "학생"
addr = "경기도 수원시"

#서식 지정자 스타일 ( C언어 방법)
print("\n========= 서식 지정자 스타일 =========")
print("이름 : %s  성별 : %s"%(name, gender))
print("나이 : %d"%age)
print("주소 : %s"%addr)

# python old style
print("\n========= python old style =========")
print("name : {} gender : {}".format(name, gender))
print("address : {} age : {}".format(addr, age))

# python recent style
print("\n========= python recent style =========")
print(f"name : {name} gender : {gender}")

#문자열 연결 연산자 사용 방식
print('name : ' + name)
print('age : '+ str(age))

# 정렬
num1 = 10
num2 = 100
num3 = 1000
num4 = 10000
num5 = 3.1415924584312434515665

print(f"|{num1:8}|")
print(f"|{num2:8}|")
print(f"|{num3:8}|")
print(f"|{num4:8}|")

print(f"{num5:.2f}")

a = input



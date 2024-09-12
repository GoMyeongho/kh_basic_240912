# 조건이 참인 동안 반복 수행

# while 문

"""

nl = n = int(input("정수를 입력하시오 : "))
sum_n = 0     # 값을 누적하기 위함


while n:    # 0이 아닌 모든 값은 참으로 간주( Java 제외 )
    sum_n += n
    n -= 1  # n = n - 1, 다른 언어에선 'n--'도 가능
print(f"1부터 {nl}까지의 모든 정수 합은 : {sum_n}")

#"""

# for 문

'''

n = int(input("정수를 입력하시오 :"))
sum_n = 0
for i in range(n):
    sum_n += i+1
print(f"1부터 {n}까지 모든 정수의 합은 {sum_n}")

#'''

# while 문은 주로 횟수가 정해지지 않은 반복적인 수행을 할 때 사용

'''

while True: # 반복문 내에 탈출 조건이 있어야 함
    age = int(input("나이를 입력하시오 : "))
    if 0 <= age <= 200: break       #정상적인 입력이므로 반복문 탈출
    print("잘못된 입력입니다.")
print(f"당신의 나이는 {age} 입니다.")

#'''

'''

while True:
    score = int(input("성적 입력 : "))
    if (score <= 100) and (score >= 0):
        if score >= 90: print("A")
        elif score >= 80: print("B")
        elif score >= 70:  print("C")
        elif score >= 60: print("D")
        else: print("F")
        break
    else:
        print('성적을 잘못 입력했습니다.')

#'''

'''

while True:
    score = int(input("성적 입력 : "))
    if (score <= 100) and (score >= 0):
        if score >= 90: grade = "A"
        elif score >= 80: grade = "B"
        elif score >= 70:  grade = "C"
        elif score >= 60: grade = "D"
        else: grade = "F"
        break
    else:
        print('성적을 잘못 입력했습니다.')
print(f"당신의 성적은 \'{grade}\' 입니다")
exit("프로그램이 완료되었습니다.")
#'''

# for 문 : 정해진 범위 만큼을 반복 수행 할 때 효과적

# for 요소 in 시퀀스:  시퀀스 자료에 대한 자동 순회,

'''

fruits = ["apple", "banana", "cherry", "mango", "watermelon"]
for fruit in fruits:
    print(fruit)

name = "vmgksdandfkldaf"
for e in name:
    print(e,end ="-")
print("\b")

for e in input("문자열을 입력하시오 : "):
    print(e, end = "-")
print('\b')

'''

# for 인덱스 in range(시작값,종료값,증감값): 범위 기반 for 문

'''

n = int(input("정수 값 입력 : "))
sum = 0
for i in range(n):      #시작 값이 0인경우 생략 가능, 증감값이 1인 경우 생략 가능
    sum += i+1
print(f"1부터 {n}까지의 합은 \'{sum}\' 입니다.")

'''

# 이중 for 문 사용하기

'''

n = int(input("정수 입력 : "))
for i in range(n):  # 0 ~ n 미만 까지
    print(f"i = {i:3}  |",end = "")
    for j in range(n):
        print("*" , end = "  ")
    print()

#'''

# 이중 for 문 구구단 찍기

'''

for i in range(2, 10):
    print()
    print("-"*20 + f"{i}단"+"-"*20)
    for j in range(1, 10):
        print(f"{i} x {j}  =  {i * j:3}",end = "\t" )
        if j % 3 == 0:
            print()

'''

# 제어문 : break, continue
# break : 반복문을 탈출 할 때 사용
# continue : 아래의 문자를 수행 하지 않고 반복 문의 조건 식으로 이동
# (해당 루틴은 수행된 것으로 간주)

'''

n = int(input("정수 입력 : "))
for i in range (n):
    if i % 2 == 0: continue     # 짝수면 아래의 문자를 수행 하지 않음
    print(i)

'''

# 반복문을 반대로 수행하기

'''

n = int(input("정수 입력 : "))
for i in range(n, 0-1, -1):     #시작값, 최종값, 증감값
    print(f"인덱스 : {i}")

'''

# for 문으로 알파벳 출력하기
# chr() : 유니코드를 입력 받아 그 코드에 해당 하는 문자를 출력
# ord() : 문자의 유니코드 값을 돌려 주는 함수

'''

code_A = ord("A")
code_a = ord("a")
for i in range(26):
    print(chr(i+code_A),end = " ")
print()
for i in range(26):
    print(chr(i + code_a), end=" ")
print()
for i in range(ord("A"), ord("z")+1):
    print(chr(i),end = " ")
    
    '''


















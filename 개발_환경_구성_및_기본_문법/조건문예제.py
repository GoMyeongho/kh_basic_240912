# 제어문이란? 조건문과 반복문의 의미


#num = int(input("정수값 입력 : "))

'''
if num >= 0:
    print(f"{num}은 양수 입니다.")
else:
    print(f"{num}은 음수 입니다.")
'''

'''
if num > 100:
    print(f"{num}은 100보다 큽니다.")
elif num == 100:
    print(f"{num}은  100입니다.")
else:
    print(f"{num}은 100보다 작습니다.")
'''

# 실습문제
# 성적을 입력 받아서 0 ~ 100 사이가 아니면 성적을 잘못 입력 하였다고 표기
# 성적이 0 ~ 100이고,
# 90 이상이면 "A"
# 80 이상이면 "B"
# 70 이상이면 "C"
# 60 이상이면 "D"
# 나머지는 "F"

'''
score = int(input("성적 입력 : "))

if (score <= 100) and (score >= 0):
    if score >= 90: print("A")
    elif score >= 80: print("B")
    elif score >= 70: print("C")
    elif score >= 60: print("D")
    else: print("F")
else:
    print('성적을 잘못 입력했습니다.')
'''


# 세자리 정수 입력 받아 100의 자리, 10의 자리, 1의 자리로 나누어 담고
# 이중 가장 큰 수 출력
# 몫과 나머지로 변수 할당
# if ~ else로 값 비교

'''
num = int(input("3자리 정수를 입력하시오 : "))

a = num // 100
b = (num % 100) // 10
c = num % 10

if 1 <= a <= 9:
    if a > b:
        if a > c: print(a)
        else: print(c)
    else:
        if b > c: print(b)
        else: print(c)
else:
    print("잘못된 입력입니다.")

num2 = list(map(int,(input("3자리 정수를 입력하시오 : "))))
print(max(num2))
'''








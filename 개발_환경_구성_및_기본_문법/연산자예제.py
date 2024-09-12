# 프로그램에서 값을 연산해야 하는 경우 사용
# 산술연산자 : +, -, *, /, //(몫), %(나머지), **(제곱)

'''
i = 10
j = 3
print( i + j )
print( i - j )
print( i * j )
print( i / j )
print( i // j )     # 몫
print( i % j )      # 나머지
print( i ** j )     # 10^3
'''

'''
TAX_RATE = 0.10     #세율
income = int(input("당신의 수입은 얼마 입니까? "))
print(f'당신이 내야 할 세금은 {income * TAX_RATE}입니다')
'''

'''
# 대입 연산자 : 값을 변수에 대입 =
# 대입 연산자의 종류 : =, +=, -=, *=, /=, %=
num1 = 10
num1 += 2       #num1 = num1 + 2
print(num1)     #12
num1 -= 10
print(num1)     #2

num1 *= 2
print(num1)     #4
'''

'''
# 비교 연산자 :
# 두개의 값을 비교해서 참/거짓을 만들어 냄
# == 같다, > 왼쪽이 크다, >= 왼쪽이 크거나 같다, <, <=

a = 10
b = 20

print(a > b)        #False
print(a < b)        #True
print(a == b)       #False
print(a >= b)       #False
print(a <= b)       #True
'''

'''
# 관계 연산자 : and(&&) 둘다 참이어야 참, or(||) 둘 중 하나만 참이면 참, not(!) 이전 상태를 부정
x = 10
y = 20
z = 30
rst1 = (x > 0) and (x > y)      # False
rst2 = (x > 0) or (x > y)       # True
rst3 = not((x > 0) or (x > y))

print(rst1)
print(rst2)
print(rst3)
'''

"""
# 3항 연산자 : 항이 3개인 연산자 : 참과 거짓이 있는 조건문 동일 >> 코드 간결, 계산에 유리
age = int(input("나이를 입력 하세요 : "))
is_adult = age > 19 and "성인" or "미성년자"
print(f"당신은 {is_adult} 입니다.")

age > 19
"""

''''''
# 비트 연산자 : 각 비트(0/1) 끼리 연산
# 2진법을 이해해야 함
#
a = 10      #00001010
b = 12      #00001100

# bit and : 둘 다 1이면
print(a & b)        #00001000 = 8
# bit or : 둘 중 하나만 1 이면
print(a | b)        #00001110 = 14
# xor 두개의 값이 다른 경우만
print(a ^ b)        #00000110 = 6
# 비트 반전 : ~
print(~a)           # -11

# 쉬프트 연산자
print(a << 1)       #00010100 = 20 (*2와 같음)
print(a >> 1)       #00000101 = 5  (//2와 같음)














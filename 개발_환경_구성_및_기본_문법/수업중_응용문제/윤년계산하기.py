# - 연도가 4로 나누어 떨어 진다.
# - 연도가 100으로 나누어 떨어지지 않는다
# - 연도가 400으로 나누어 떨어진다

year = int(input("년도를 입력하세요 : "))
'''
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year}는 윤년입니다")
        else:
            print(f"{year}는 윤년이 아닙니다")
    else:
        print(f"{year}는 윤년입니다")
else:
    print(f"{year}는 윤년이 아닙니다")

# if else를 이용한 풀이
'''

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year}는 윤년입니다")
else:
    print(f"{year}는 윤년이 아닙니다")

# 3중 연산자를 이용한 풀이




n = int(input("정수 'n'을 입력 하시오 : "))
while True:
    temp = int(input("수를 입력 하시오 : "))
    if temp == 0: break
    if temp % n == 0:
        print(f"{temp} is a multiple of {n}.")
    else:
        print(f"{temp} is NOT a multiple of {n}.")





















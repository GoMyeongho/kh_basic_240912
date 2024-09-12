# 양의 정수 n을 입력받아 n * n 크기의 행렬을 출력하는 프로그램 작성
# 이때 행렬의 값은 1부터 시작하여 왼쪽에서 오른쪽, 위에서 아래 순서대로 채워 넣음
# 입력 :
from math import log10

# 1. 입력받은 값으로 실제 출력 범위를 정해야 함
# 2. 줄바꿈에 대한 처리(나머지 연산자 사용)
# 3. 줄맞춤


#'''

while True:
    n = int(input("정수를 입력하시오 : "))
    if n > 0:
        # n_digit = 3 + int(log10(n * n))
        n_digit = 2 + len(str(n*n))
        for i in range(n):
            for j in range(n):
                num =i * n + j + 1
                print(f"{num:{n_digit}}", end="")
            print()
        break
    else:
        print("잘못된 입력입니다.")
        
#'''

'''

n = int(input("정수 입력 :"))
for i  in range(n*n):
    print(f"{i+1:5}", end = "")
    if i % n == n-1: print()

'''






















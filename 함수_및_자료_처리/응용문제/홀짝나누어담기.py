# 무작위 수를 공백 기준으로 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력 하는 문제

# 내 풀이

"""

num_list = list(map(int,input("정수를 입력 하시오 : ").split()))
even_list = []
odd_list = []

for e in num_list:
    if e % 2 == 0: even_list.append(e)
    else: odd_list.append(e)

print(f"홀수는 {odd_list} 입니다. \n 짝수는 {even_list} 입니다.")

"""

# 강사님 풀이

"""

num_list = list(map(int,input("정수를 입력 하시오 : ").split()))
even_list = list(filter(lambda x: x % 2 == 0, num_list))
odd_list = list(filter(lambda x: x % 2 == 1, num_list))

print(f"홀수는 {odd_list} 입니다. \n 짝수는 {even_list} 입니다.")

"""









































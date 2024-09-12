# 자연수 A, B, C
# A = 150, B = 266, C = 427이라면 A x B x C  = 150 x 266 x 427 = 170037300
#각각의 등장하는 숫자(0~9)의 갯수를 세는 문제 :


"""

A = int(input("정수 A를 입력하시오 :"))
B = int(input("정수 B를 입력하시오 :"))
C = int(input("정수 C를 입력하시오 :"))

multi = str(A * B * C)
for i in range(10):
    print(f"{i} : {multi.count(f'{i}')}개")
                                #str(i)
"""

# 실습 2번 : 문자열 반전, 문자열을 입력 받아서 문자열 반전 출력
# EX) ABCDEF => FEDCBA

'''

D = input("문자열을 입력하시오")
E =''
for i in range(len(D)-1, -1, -1):
    E += D[i]
print(E)

'''











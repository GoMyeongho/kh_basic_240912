# 2개읠 문자열을 포인터 변수 s와 K에, 양의 정수를 정수형 변수
# n에 각각 전달받아 s 문자열 뒤 부분의 n개 문자를 k 문자열 앞에 끼워넣는 코드 작성
# 예)    s :     seoul
#        k :     korea
#        n :     2
#        result : ulkorea

s = input("s : " )
k = input("k : ")
n = int(input("n : "))

a = s[-n:] + k
print(a)









































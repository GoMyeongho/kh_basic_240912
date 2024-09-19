fibo = [1,1]
n = int(input("피보나치 수열의 항의 개수를 입력 하시오 : "))
while len(fibo) < n:
    fibo.append(fibo[len(fibo)-1]+fibo[len(fibo)-2])
print(fibo)
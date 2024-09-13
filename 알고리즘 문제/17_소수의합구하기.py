n = int(input())
prime_n = [2]
sum = 2
for i in range(3,n):
    prime = True
    for e in prime_n:
        if i % e == 0:
            prime = False
    if prime:
        sum += i
        prime_n.append(i)

print(sum)















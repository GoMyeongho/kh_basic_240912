n = int(input())
prime_n = [2]
prime_sum = 2
for i in range(3,n):
    prime = True
    for e in prime_n:
        if i % e == 0:
            prime = False
    if prime:
        prime_sum += i
        prime_n.append(i)

print(prime_sum)















import random
lotto = []
i = 0
while i < 6:
    lotto[i] = random.randrange(1,46)
    for j in range(i):
        if lotto[i] == lotto[j]:
            i -= 1
            break
    i += 1

print(lotto)








































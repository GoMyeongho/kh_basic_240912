from itertools import count

C = int(input("테스트 케이스 종류 : "))
for i in range(C):
    test = list(map(int, input().split()))
    mean = sum(test[1:])/(len(test)-1)
    count = 0
    for e in test[1:]:
        if e > mean:
            count += 1
    rate = 100 * count/(len(test)-1)
    print(f'{rate:.3f}%')



















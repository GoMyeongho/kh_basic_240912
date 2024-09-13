# 외장함수는 import 해서 사용 하는 함수, 파이썬이 기본적으로 제공 하는 것

# 랜덤 함수 : 지정한 범위 내에서 임의의 숫자를 만들어 내는 것

import random

"""

for i in range(30):
    rand1 = random.randint(0,4)             # 0 ~ 4까지의 임의의 값을 생성
    print(rand1 , end=" ")
print()

for i in range(30):
    rand1 = random.randrange(0, 10)  # 0 ~ 10 미만
    print(rand1, end=" ")
print()

"""

# 중복되지 않는 로또번호 만들기 : 1 ~ 45사이의 임의의 수 6개
# 리스트를 사용 하고, 리스트 내에 임의로 생성한 번호가 있으면, 추가 X

"""

lotto = []
n = 0
while n < 6:
    temp = random.randrange(1, 46)
    if lotto.count(temp) > 0:
        continue
    lotto[n] = temp
    n += 1
    # if temp not in lotto
    #   lotto.append(lotto)
    # if len(lotto) == 6: break
print(lotto)

lotto = set()
while len(lotto) < 6:
    rand = random.randrange(1, 46)
    lotto.add(rand)
print(lotto)

#"""



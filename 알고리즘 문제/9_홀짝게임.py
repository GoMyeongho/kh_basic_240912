import random

dice1 = random.randrange(1,7)
dice2 = random.randrange(1,7)
dice_sum = dice1 + dice2

if dice_sum % 2 == 0:
    print("짝!")
    if dice1 == dice2:
        print("더블!")
else:
    print("홀!")










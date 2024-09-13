
def color2num(color):
    if color == 'black': n = 0
    elif color == "brown": n = 1
    elif color == "red": n = 2
    elif color == "orange": n = 3
    elif color == "yellow": n = 4
    elif color == "green": n = 5
    elif color == "blue": n = 6
    elif color == "violet": n = 7
    elif color == "grey": n = 8
    elif color == "white": n = 9
    else: print("잘못된 입력입니다")
    return n

n1 = color2num(input())
n2 = color2num(input())
n3 = color2num(input())

resist = (n1* 10 + n2) * 10 ** (n3)
print(resist)


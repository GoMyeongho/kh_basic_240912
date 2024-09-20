num_8 = input()
num_2 =""
for i in num_8:
    num_2 += str(int(i) // 4)
    num_2 += str(int(i) % 4 // 2)
    num_2 += str(int(i) % 2)
print(int(num_2))













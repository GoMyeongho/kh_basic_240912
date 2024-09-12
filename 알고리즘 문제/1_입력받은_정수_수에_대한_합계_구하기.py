int_num  = int(input("정수의 개수를 입력하시오 :"))
sum = 0
for i in range(int_num):
    sum += int(input(f"{i+1}번째 정수를 기입하시오 : "))
print(sum)


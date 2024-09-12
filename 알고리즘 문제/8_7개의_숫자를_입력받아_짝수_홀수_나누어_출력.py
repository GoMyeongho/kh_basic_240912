nums = list(map(int,input("정수 7개를 입력하시오 : ").split((" "))))

odd = []
even = []

for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"짝수는 {even} 입니다 ")
print(f"홀수는 {odd} 입니다 ")









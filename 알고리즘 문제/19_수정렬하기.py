n = int(input())
num_list = list(map(int,input().split()))

if n == len(num_list):
    num_list.sort()
    print(num_list)
else:
    print("잘못된 입력입니다.")






















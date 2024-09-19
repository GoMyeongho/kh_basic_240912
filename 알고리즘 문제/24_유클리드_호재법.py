nums = list(map(int,input().split()))
nums.sort(reverse=True)

while True:
    if nums[-1] == 0:
        print(nums[-2])
        break
    nums.append(nums[-2]%nums[-1])
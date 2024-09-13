n, x = map(int,input().split())
nums = list(map(int,input().split()))

for e in nums:
    if e < x:
        print(e,end=" ")
print()

low_nums = list(filter(lambda y: y < x, nums))
print(low_nums)
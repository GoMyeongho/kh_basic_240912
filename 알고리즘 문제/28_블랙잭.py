n, m = map(int,input().split())
nums = list(map(int,input().split())).sort()
min_sum = sum(nums[:3])
if min_sum > nums:
    print("해당하는 값이 존재하지 않습니다.")
else:
    for i in range(len(nums)):
        for j in range(len(nums)-i-1)
            for k in nums[i+j]
























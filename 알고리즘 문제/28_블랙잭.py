n, m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
min_sum = sum(nums[:3])

if min_sum > m:
    print("해당하는 값이 존재하지 않습니다.")
else:
    nums_sum = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(i+j+1,len(nums)):
                if nums[i]+nums[j]+nums[k] > m: break
                if nums_sum < nums[i]+nums[j]+nums[k]: nums_sum = nums[i]+nums[j]+nums[k]
    print(nums_sum)
























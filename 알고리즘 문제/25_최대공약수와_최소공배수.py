nums = list(map(int,input().split()))
nums.sort(reverse=True)

while True:
    if nums[-1] == 0:
        break
    nums.append(nums[-2]%nums[-1])

max_common_div = nums[-2]
min_common_mult = nums[0] * nums[1] // max_common_div

print(f"최대 공배수 : {max_common_div}")
print(f"최소 공약수 : {min_common_mult}")
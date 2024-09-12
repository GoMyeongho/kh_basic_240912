nums = list(map(int,input("숫자들을 입력하시오 : ").split(" ")))

max_num = max(nums)
min_num = min(nums)

'''
max_num = nums[0]
min_num = nums[0]
for i in nums:
    if max_num < i: max_num = i
    if min_num > i: min_num = i
#'''

print(f'''
최댓값은 {max_num} 이고,
최솟값은 {min_num} 입니다.
''')










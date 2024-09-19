# 두번째 수 찾기
# 입력 : 1 2 3 4 5 6 7 8 3 4 5 6 7 8
# 찾을 수 : 3
# 해당 수의 위치를 반환 : 인덱스가 아닌, 9번쨰
# 찾지 못하면 -1

def second_find(ls, n):
    if ls.count(n) > 1:
        idx = ls.index(n) + 1
        return ls[idx:].index(n) + idx + 1
    else:
        return -1


num_list = list(map(int,input().split()))
num = int(input())

print(second_find(num_list,num))





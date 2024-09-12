
# 입력 : 5
# *
# **
# ***
# ****
# *****
from skimage.graph import rag_mean_color

star = int(input("별의 층수를 입력하시오 : "))

for i in range(star):
    for j in range (i+1):
        print("*",end="")
    print()


#'''

#2중 for 문 안쓰고 해보기
stars = (star*(star+1))//2
n = 0
m = 0
for i in range(stars):
    if n > m:
        n = 0
        m += 1
        print()
    print("*",end="")
    n += 1
print()
#'''
for i in range(star):
    for j in range(star-i):
        print(" ",end="")
    for k in range (2*i+1):
        print("*",end="")
    print()







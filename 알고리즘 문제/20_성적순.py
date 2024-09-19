student_num = int(input())
names = []
for i in range(student_num):
    name , score = input().split()
    score = int(score)
    names.append([name, score])
names.sort(key = lambda x:x[1])
for name,score in names:
    print(name,end = " ")








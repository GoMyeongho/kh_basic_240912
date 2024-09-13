score = []
for i in range(5):
    temp = int(input("학생의 성적을 입력 하시오 : "))
    if temp < 40:
        temp = 40
    score.append(temp)
mean_score = sum(score)/len(score)
print(mean_score)






















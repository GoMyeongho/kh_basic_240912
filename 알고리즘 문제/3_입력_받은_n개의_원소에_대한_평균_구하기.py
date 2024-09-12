n = int(input("변수의 개수는?"))
score = list(map(int,input('점수는 : ').split(" ")))
if len(score) != n:
    print("잘못된 입력입니다")
else:
    print(sum(score)/len(score))

























# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤,
# 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오
# isLower() : 소문자이면 True, 아니면 False


a = input("문자열을 입력하시오 :")


n_a = ''
for i in a:
    if i == i.upper():
        n_a += i.lower()
    else:
        n_a += i.upper()



print("변환된 문장 : " + n_a)







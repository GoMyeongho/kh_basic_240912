# 회원 가입을 위한 아이디 패스워드 입력 받기
id = input("아이디 입력 : ")

if len(id) >= 8:
    pw = input("비밀번호 입력 :")
    if not 8 <= len(pw) <= 16:
        print('비밀번호는 8자리와 16자리 사이여야 합니다.')
    elif pw.find(id) >= 0:
        print("비밀번호에 아이디를 포함할 수 없습니다.")
    else:
        print(f"아이디 : {id}")
        print(f"비밀번호 : {pw}")
else:
    print("아이디는 반드시 8자리 이상이여야 합니다.")








































#주석은 인터프리팅 안하는 영역
print('파이썬을 공부하겠습니다.') #이 부분은 '주석' 입니다.
print(100)
print(33.3333)
print(100 + 200)
print(100 < 200)

#파이썬은 값이 대입될 때 데이터형이 결정됨, '', "", 둘다 문자열을 의미
#파이썬 문자를 따로 구분하지 않음

# == 같다, = 대입한다

name = '고명호'
print(name)

"""
범위주석
"""

'''
식별자 생성 규칙
 * 키워드(예약어) 는 사용 금지.
 * 특수문자는 '_'(언더바)만 사용 가능하다.
 * 숫자는 사용 가능 하지만 맨 앞에 와선 안된다.
 * snake_case : 스네이크 표기법을 따름, 단어와 단어를 연결할 때 _ 사용한다.
 class 이름은 대문자로 시작
'''

tax_rate = 0.1  #python
taxRate = 0.1   #java
TaxRate = 0.1

name = '고명호'
email = 'sdx02013@ajou.ac.kr'
phone = '010-5015-4852'
addr = '경기도 수원시 권선구'
print(f"""
    이름 : {name}
    이메일 : {email}
    전화번호 : {phone}
    주소 : {addr}
""")

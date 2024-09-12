# 문자열이란? 문자로 이루어진 데이터의 집합
# "", '', """ """, ''' '''
# 인덱싱 : 시퀀스(리스트, 튜플, 문자열, input()) 자료형에서 특정 위치의 요소를 선택하는 작업
# 인덱싱은 0 부터 시작
# 슬라이싱 : 시퀀스 자료형에서 일부 데이터를 추출하는 것 (잘라내는 것)

'''

jumin = input("주민등록번호 입력 : ")     #991120-1234567

gender = int(jumin[7])
if gender % 2 == 1:
    print("남성 입니다.")
else:
    print("여성 입니다.")
#print(gender)

#태어난 년도를 구하기 위해서 슬라이싱
year = jumin[:2]   # 0에서 2 미만 [시작 인덱스 : 미만(본인제외)] , 0에서부터 시작되는 경우는 생략가능
cent = 19 + (gender-1)//2
print("탄생년도는 " + str(cent)+year+"년입니다")

# 생일 출력

month = int(jumin[2:4])
day = int(jumin[4:6])

print( f"생일은 {month}월 {day}일입니다.")

#생년월일
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:]) #-1은 맨 뒷자리

#print(jumin[14]) 는 out of range 에러가 뜬다.

'''

life = "Life is too short, You need Python"
tmp = life[0] + life[1] + life [2] + life[3]
print(tmp)

#대소문자 바꾸기 : upper(), lower()

a = "Hello Python Program..."

print("a.upper() = " + a.upper())
print("a.lower() = " + a.lower())

#대문자는 소문자로 소문자는 대문자로



# for i in a:
#     if i == i.upper():
#         a = a.replace(i,i.lower())
#     else:
#         a = a.replace(i,i.upper())

n_a = ''
for i in a:
    if i == i.upper():
        n_a += i.lower()
    else:
        n_a += i.upper()



print("reversed a : " + n_a)





# 문자열 변경 : replace("기존 문자열", "바꿀 문자열")

b = "Hello Python Program..."
n_b = b.replace("Python","JavaScript")
print(n_b)

# 문자열에 포함된 문자 갯수 세기 및 문자열 길이 구하기
# count() : 문자열 내장 함수로 문자열에 포함된 문자의 갯수를 반환
# __len__() 문자열 길이를 반환
# len() : 문자열 길이를 반환
c = "Hello Python Python Program..."
print(c.count("l")) #해당 문자열에서 매개변수로 전달한 문자/문자열의 갯수를 반환
print(len(c)) #문자열의 길이를 반환
print(c.__len__())

# 문자열 찾기 : find(), rfind(), index()
# find() : 찾은 문자열의 시작 인덱스 반한 찾지 못하면 -1
# index() : 찾은 문자열의 시작 인덱스 반환, 찾지 못하면 ValueError 발생하고 종료됨
# rfind() : 뒤에서부터 문자열을 찾음, 찾은 문자열의 인덱스는 앞에서 부터 계산

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점찾기, 가장 좋은 선물은 용기"
print(phrase.find("가장"))
print(phrase.rfind("가장"))
print(phrase.index("포기"))

print(phrase.find("나에게"))

new_phrase = phrase.replace("가장","나에게")
print(new_phrase)


# 문자열 연산자 ; + , *
def sum_ex(x, y):
    return x + y
print(sum_ex(100, 200))
print(sum_ex(100, 200))
print(sum_ex("Korea", "Seoul"))

print("!"*10)
list = [0] * 10
print(list)

#문자열의 양 옆의 공백제거 : strip()

d = '''
        안녕하세요.
        문자열의 공백을 제거하겠습니다.
        네네네.........                   
'''
print(d.strip())





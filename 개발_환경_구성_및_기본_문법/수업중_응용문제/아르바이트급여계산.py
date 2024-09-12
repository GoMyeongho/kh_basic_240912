# 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 근무 시급 : 9860원
# 야간 근무 시급 : 주간 시급 * 1.5
# [입력] 주간근무 [1] 야간근무[2] 를 입력 하세요 :
# [입력] 근무 시간을 입력 하세요 :
# [출력] print(f'{근무시간}시간 동안 근무한 {근무타입문자열} 급여는 {급여}원 입니다.')


work_type = input("주간근무 [1] 야간근무[2] 를 입력 하세요 : ")


if work_type == '1':
    work_type = '주간근무'
    hour_pay = 9860
elif work_type == '2':
    work_type = '야간근무'
    hour_pay = 9860 *1.5
else:
    print("잘못된 입력입니다.")
    exit(0)

work_hour = int(input("근무 시간을 입력 하세요 :"))
pay = work_hour * hour_pay
print(f'{work_hour}시간 동안 근무한 {work_type} 급여는 {pay}원 입니다.')




























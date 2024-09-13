# 영식(Y) 요금제 : 30초마다 10원 청구
# 민식(M) 요금제 : 60초마다 15원
# 3 <= 통화 횟수
# 40 40 40 각 통화당 통화시간
# M 45 <더 싼 요금제와 통화 요금
import numpy as np


# 통화 횟수 입력

# 각 통화에 대한 통화 시간 입력

# 통화시간에 대한 리스트를 순회하면서 총 통화 시간 누적
# 민식과 영식 요금제에 대한 총 통화 요금을 누적하고 둘 중 싼 것을 찾아야 함
# 만약 같은 경우 Y M 으로 출력



call_num = int(input("통화 횟수 :"))
call_sec = list(map(int, input("각 통화당 통화 시간 : ").split()))

array_sec = np.array(call_sec)
y_pay = sum(((array_sec // 30) + 1)* 10)
m_pay = sum(((array_sec // 60) + 1)* 15)

if y_pay < m_pay:
    print(f"영식 요금제로 {y_pay}")
elif y_pay == m_pay:
    print(f"영식 요금제 또는 민식 요금제로 {y_pay}")
else:
    print(f"민식 요금제로 {m_pay}")

M_pay = Y_pay = 0

for e in call_sec:
    Y_pay += (e // 30 + 1) * 10
    M_pay += (e // 60 + 1) * 15

if Y_pay < M_pay:
    print(f"영식 요금제로 {Y_pay}")
elif Y_pay == M_pay:
    print(f"영식 요금제 또는 민식 요금제로 {Y_pay}")
else:
    print(f"민식 요금제로 {M_pay}")






























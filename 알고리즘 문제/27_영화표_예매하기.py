seat_list = [0]*10

while True:
    for e in seat_list:
        print("[V]", end=" ") if e == 1 else print("[ ]", end=" ")
    print()
    menu = int(input("[1]예매하기, [2]종료하기\n"))
    if menu == 2: break
    seat_idx = int(input("좌석 번호를 입력 하시오 : ")) - 1
    if seat_list[seat_idx] == 0:
        seat_list[seat_idx] = 1
    else:
        print("이미 예매된 좌석 입니다.")

for e in seat_list:
    print("[V]",end=" ") if e == 1 else print("[ ]",end=" ")
print()
print(f"총 매출액 : {12000 * seat_list.count(1)}")





















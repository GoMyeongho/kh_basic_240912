import math

class Car:
    dist = [400, 200, 150, 300]
    def __init__(self):
        self.efficiency = self.speed = self.tank = self.tank = self.seat = self.ability = 0

    def abil(self):
        if self.ability == 1: self.speed *= 1.2
        elif self.ability == 2: self.seat += 1
        elif self.ability == 3: self.tank += 30

    def total_move(self,passenger):
        return math.ceil(passenger // self.seat)

    def total_tank(self, dest):
        return Car.dist[dest] / self.efficiency

    def fuel_count(self, dest, passenger):
        return math.ceil(self.total_tank(dest) * self.total_move(passenger) / self.tank)

    def total_pay(self,dest,passenger):
        return round(2000 * self.total_tank(dest) * self.total_move(passenger))

    def total_time(self,dest,passenger):
        return Car.dist[dest] * self.total_move(passenger) / self.speed

class SportsCar(Car):

    def __init__(self):
        self.name = "Ferrari"
        self.efficiency = 8
        self.speed = 250
        self.tank = 30
        self.seat = 2
        self.ability = 1

class Sedan(Car):

    def __init__(self):
        self.name = "GV80"
        self.efficiency = 12
        self.speed = 200
        self.tank = 45
        self.seat = 4
        self.ability = 2

class Bus(Car):

    def __init__(self):
        self.name = "관광버스"
        self.efficiency = 5
        self.speed = 150
        self.tank = 100
        self.seat = 20
        self.ability = 3

def hour_min_list(time):
    hour = round (time // 1)
    min = round((time - time // 1 ) * 60)
    return [hour,min]

count = 0
while True:
    if count < 1:
        destination = int(input("이동 지역을 선택 하세요 (1. 부산, 2. 대전, 3. 강릉, 4. 광주) ")) - 1
        if destination not in [0, 1, 2, 3]:
            print("잘못된 입력 입니다.")
            continue
        count += 1
    if count < 2:
        num_passenger = int(input("이동할 승객 수를 입력 하세요 ( 1 ~ 100 사이)"))
        if 1 <= num_passenger <= 100:
            count += 1
        else:
            print("잘못된 입력 입니다.")
            continue
    if count < 3:
        car_kind = input("이동 차량을 선택 하세요. (1. 스포츠카, 2.승용차, 3번 버스)")
        if car_kind not in ["1", "2", "3"]:
            print("잘못된 입력 입니다.")
            continue
        count += 1
    ability_on = input("부가 기능의 ON[1]/OFF[2] 를 선택 하세요")
    if ability_on not in ["1", "2"]:
        continue
    break

if car_kind == "1":
    new_car = SportsCar()
elif car_kind == "2":
    new_car = Sedan()
elif car_kind == "3":
    new_car = Bus()

if ability_on == "1": new_car.abil()

print(f"""
====={new_car.name}=====
총 비용 : {new_car.total_pay(destination,num_passenger)}
총 주유 횟수 : {new_car.fuel_count(destination,num_passenger)}
총 이동 시간 : {hour_min_list(new_car.total_time(destination,num_passenger))[0]}시 {hour_min_list(new_car.total_time(destination,num_passenger))[1]}분          
""")

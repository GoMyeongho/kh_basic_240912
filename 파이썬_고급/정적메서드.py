# 인스턴스 메서드 : 객체로 만들어 질 때 함께 만들어지는 메서드
# 정적 메서드 : 클래스와 관련이 있음, 객체와 무관한 독립적인 동작 수행
# 클래스 매서드 : 클래스와 관련 있음, 클래스 변수를 사용하기 위함

class Car:
    is_instance_cnt = 0     # 클래스 변수(맴버), 클래스 소속, 객체로 만들어 지지 않음

    def __init__(self, size, model):
        self.size = size
        self.model = model
        self.speed = 0
        Car.is_instance_cnt += 1    #클래스 변수 사용
        print(f"자동차 객체 생숭 수 : {Car.is_instance_cnt}")


    def move(self, speed):
        self.speed = speed
        print(f"자동차 {self.size} & {self.model}이 시속 {self.speed}로 달립니다.")






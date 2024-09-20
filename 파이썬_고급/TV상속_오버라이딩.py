# 다형성이란 부모가 물려 준 특성을 재정의 사용하는 것을 의미
# 오버로딩 : 파이썬에서 지원하지 않음 (메서드 이름을 동일하고 매개변수의 갯수나 타입으로 구분)
# 오버라이딩 : 부모가 물려준 특성을 재정의 하는것


"""

def over_sum(x, y, z):
    return x + y + z

print(over_sum(1,2,3))
print(over_sum(1.1,2.2,3.3))
print(over_sum("혜인","하나","가을"))

"""

class PrototypeTV:
    def __init__(self, is_on, channel, volume):
        self.is_on = is_on
        self.channel = channel
        self.volume = volume

    def set_on(self, is_on):
        self.is_on = is_on

    def set_channel(self, cnl):
        if 1 <= cnl <= 1000:
            self.channel = cnl
            print(f"채널을 {self.channel}로 변경 하였습니다")
        else:
            print("체널 설정 범위가 아닙니다.")

class ProductTv(PrototypeTV):
    def set_channel(self, cnl):
        if 1 <= cnl <= 2000:
            self.channel = cnl
            print(f"채널을 {self.channel}로 변경 하였습니다")
        else:
            print("체널 설정 범위가 아닙니다.")


lg_tv = ProductTv(False,20, 20)
lg_tv.set_channel(1500)















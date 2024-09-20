# 클래스란 객체를 만들기 위한 설계 도면, 상태값을 저장하는 변수(인스턴스)
# 동작을 규정하는 메서드가 포함
# 키워드는 class
# 객체란 클래스를 실체화 한 것
# 상속 : 부모 클래스의 특성을 자식 클래스에 물려주는 것
# 캡슐화 : 내부의 멤버(변수)를 외부에서 접근 할 수 없도록 하는 것
# 접근을 위한 게터와 세터 메서트 필요
# 다형성 : 부모의 특성을 물려받아 특성을 변경하거나 개선하는 행위
# 파이썬에선 오버로딩은 없고 오버라이딩만 있다.
# 추상화 : 객체화가 되지 않는 부모로부터 특성을 물려 받는 것(추상 클래스)
# 클래스의 이름 파스칼표기법(첫자가 대문자 혹은 전체가 대문자)
# 클래스를 만들기 위해서 생성자가 필요(__init__)
# 생성자는 클래스가 객체로 만들어 질 때 불려짐
# 내부의 인스턴스 변수를 초기화하는 목적으로 사용

class TeleVision:
    def __init__(self, name, is_on, channel, volume):
        self.name = name    # 인스턴스 변수를 생성하고 생성자의 매개변수 변수를 통해서 초기값을 입력받음
        self.is_on = is_on
        self.channel = channel
        self.volume = volume

    def set_on(self, is_on):
        self.is_on = is_on

    def set_channel(self, channel):
        self.channel = channel

    def set_volume(self, volume):
        self.volume = volume

    def tv_info(self):
        power = ("OFF", "ON")
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.is_on]}")
        print(f"체널 : {self.channel}")
        print(f"볼륨 : {self.volume}")

lg_tv1 = TeleVision("우리집TV", False, 11, 10)
lg_tv2 = TeleVision("우리집TV", False, 11, 10)

lg_tv1.set_on(True)
lg_tv1.set_volume(50)
lg_tv1.tv_info()
















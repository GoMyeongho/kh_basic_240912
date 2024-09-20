# 추상화란? 실체하가 되지 않는 부모로부터 상속 받는 것.
# 부모 클래스 에서 이름만 선언되고 구현부가 없는 추상 메서드를 포함
# 상속 받은 클래스는 반드시 추상 메서드에 대해서 구현 해줘야 함.
# 외부 프로그램의 알고리즘을 알지 않아도 코드가 구현하기 위해
from abc import *   # 추상 클래스를 사용하기 위해 import


class NetworkAdapter(metaclass=ABCMeta):    # 해당 클래스를 추상 클래스로 만듦
    @abstractmethod
    def connect(self):
        pass

class WiFi(NetworkAdapter):
    def __init__(self,company):
        self.company = company

    def connect(self):
        print(f"{self.company}의 Wi-Fi에 연결 되었습니다")

class FiveG(NetworkAdapter):
    def __init__(self,company):
        self.company = company

    def connect(self):
        print(f"{self.company}의 5G에 연결 되었습니다")


class Lte(NetworkAdapter):
    def __init__(self,company):
        self.company = company

    def connect(self):
        print(f"{self.company}의 LTE에 연결 되었습니다")

net = input("연결할 네트워크 [1] Wi-Fi [2] 5G [3] LTE")


if net == "1":
    adapter = WiFi("KT Megapass")

elif net == "2":
    adapter = FiveG("Sk Telecom")

elif net == "3":
    adapter = Lte("LG U+")

else: print("잘못된 입력 입니다.")

adapter.connect()


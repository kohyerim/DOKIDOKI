from . import coin
from . import powerups as p


class Keyboard(coin.Coin):
    def __init__(self):
        pass


class Mouse(coin.Coin):
    def __init__(self):
        pass

    def adding_score(self):
        pass


class PLBook(coin.Coin):
    pass


class Virus(coin.Coin):
    pass


class Error(coin.Coin):
    pass


class Hotsix(p.Star):
    pass


# Coin 클래스 안에 spinning 함수 오버라이딩 하거나 아예 새로운 함수 만들기
# 지금은 있는거 없애도 상관없음 아예 coin 클래스 참고하면서 새로운 클래스 ?

# import는 뭔가요 ~ 라이브러리 불러오기 입니다 C언어에서 #include 느낌?
# from data import main 은 data폴더의 main 라이브러리를 불러오는 거에요 사용자가 만든 라이브러리 불러올 때 이렇게 해요
# as는 뭔가요~ 이름이 너무 길어서 as 뭐뭐로 바꿔서 부르겠다는 뜻이에요

from data import main
from data import menu
from data import config as c
import pygame as pg
import os
import sys


class App():
    def __init__(self):  # __init__ 함수는 객체를 새로 만들 때 초기화 하는거에요 생성자 함수!!!!!
        self.menu = None # self는 이 클래스로 만든 객체 자신을 불러올 때? 쓰는거에요 
        self.main = None

    def run(self):
        self.menu = menu.Menu() # menu.Menu() 는 위에서 import한 menu 라이브러리에 있는 Menu 함수를 호출한거!
        self.menu.menu_loop() # 위에 꺼랑 비슷한 맥락이겟조 
        if self.menu.quit_state == 'play': #Check whether to continue to game or quit app
            self.main = main.Main()
            self.main.main_loop()
            if self.main.quit_state == 'menu':
                #If you think this is a cheat 
                #to avoid destroying instances,
                #you are right, I'm just too
                #lazy to do that.
                os.execl(sys.executable, sys.executable, *sys.argv) #Restart game


if __name__ == '__main__': # 이거는 메인함수 사실 파이썬에서 안써도 되기는 한데 어디서 실행되는지 명확해야 되니까 쓰는게 좋겠다
    pg.init() #Initialize pygame module
    c.screen = pg.display.set_mode((c.SCREEN_SIZE.x, c.SCREEN_SIZE.y))
    pg.display.set_caption(c.CAPTION)
    c.clock = pg.time.Clock()

    app = App()
    app.run()

    pg.quit()

# 사실 ㅇㅕ기서는 별로 공부할 거는 없어요 .. 왜냐면 data 폴더 안에 있는 것들을 가져와서 실행하는거 니까 !
# 중요한 거는 data 안에 있는 라이브러리 들이고 그거를 주로 공부하는 것이 좋을 거 같습니다잉
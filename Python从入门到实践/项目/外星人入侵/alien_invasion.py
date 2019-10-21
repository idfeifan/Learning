# coding=utf-8
import pygame
from Python从入门到实践.项目.外星人入侵.settings import Settings
from Python从入门到实践.项目.外星人入侵.ship import Ship
import Python从入门到实践.项目.外星人入侵.game_functions as gf
def run_game():
    '''初始化游戏并创建屏幕对象'''
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_height,ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")


    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()

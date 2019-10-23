# coding=utf-8
import pygame
#类的实例类似列表提供了有助于开发游戏的额外功能
from pygame.sprite import Group
from Python从入门到实践.项目.外星人入侵.settings import Settings
from Python从入门到实践.项目.外星人入侵.ship import Ship
from Python从入门到实践.项目.外星人入侵.bullet import Bullet
import Python从入门到实践.项目.外星人入侵.game_functions as gf
def run_game():
    '''初始化游戏并创建屏幕对象'''
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_height,ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")


    #创建一艘飞船、一个子弹编组 和 一个外星人编组
    ship = Ship(ai_settings,screen)

    bullets = Group()

    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update() #更新飞船的位置
        gf.update_bullets(bullets) #所有未消失的子弹的位置
        gf.update_aliens(aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets) #更新后的位置来绘制屏幕



if __name__ == "__main__":
    run_game()

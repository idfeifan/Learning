# coding=utf-8
class Settings():
    '''存储《外星人入侵》的所有设置的类'''
    def __init__(self):
        '''初始化游戏的设置'''

        #设置屏幕
        self.screen_width = 790
        self.screen_height = 700
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60

        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 0.3
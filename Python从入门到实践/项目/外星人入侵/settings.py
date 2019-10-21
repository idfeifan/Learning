# coding=utf-8
class Settings():
    '''存储《外星人入侵》的所有设置的类'''
    def __init__(self):
        '''初始化游戏的设置'''

        #设置屏幕
        self.screen_width = 700
        self.screen_height = 1000
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
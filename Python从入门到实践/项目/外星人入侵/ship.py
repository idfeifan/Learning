# coding=utf-8
import pygame
'''管理飞船大部分行为'''
class Ship():

    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        #返回surface对象
        self.image = pygame.image.load('E:\Pwork\Learning\Python从入门到实践\项目\外星人入侵\image\ship.bmp')
        self.rect = self.image.get_rect() #获取surface的rect属性 理解为图片的矩形
        self.screen_rect = screen.get_rect() # 获取背景的rect矩形

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx #图片
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        #根据self.center跟新到rect对象

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
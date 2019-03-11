#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对子弹进行管理的类"""

    def __init__(self, screen, game_settings, ship):
        """
        子弹的类属性，在飞船所处的位置创建一个子弹对象
        """
        super(Bullet, self).__init__()  # 继承Sprite类
        self.screen = screen

        # 在坐标(0,0)处创建一个子弹矩形，在设置到正确的位置
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width,
                                game_settings.bullet_height)

        # 把创建的子弹矩形设置到飞船的顶部中心的位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)  # 把子弹的y坐标设置成小数

        # 设置子弹的颜色和速度
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self, *args):
        """更新子弹的位置，子弹是向上移动的"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.rect, self.color)










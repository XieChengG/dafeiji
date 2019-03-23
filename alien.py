#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """单个外星人的类"""
    def __init__(self, screen, game_settings):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load_basic('images/alien.bmp')  # 加载外星人图像
        self.rect = self.image.get_rect()  # 获取外星人图像的外接矩形位置

        # 获取外星人在屏幕左上角位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)  # 横坐标存储为浮点型，

    def blitme(self):
        """在屏幕上的指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """检查外星人是否位于屏幕的边缘"""
        screen_rect = self.screen.rect  # 获取屏幕边缘

        # 如果有外星人位于屏幕的左边缘或右边缘，都返回True
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向右移动外星人"""
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction)
        self.rect.x = self.x








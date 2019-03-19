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








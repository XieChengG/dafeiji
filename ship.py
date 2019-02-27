#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pygame

class Ship(object):

    def __init__(self, screen):
        """
        1.加载飞船图像
        2.设置飞船在屏幕上的位置
        :param screen:
        """
        self.screen = screen
        self.image = pygame.image.load_basic('images/ship.bmp')
        self.rect = self.image.get_rect()  # 获取图像的外接矩形
        self.screen_rect = screen.get_rect()  # 获取屏幕的外接矩形

        # 将飞船的位置设置在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """
        在指定位置绘制飞船
        :return:
        """
        self.screen.blit(self.image, self.rect)






#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pygame


class Ship(object):

    def __init__(self, game_settings, screen):
        """
        1.加载飞船图像
        2.设置飞船在屏幕上的位置
        :param screen:
        """
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load_basic('images/ship.bmp')
        self.rect = self.image.get_rect()  # 获取图像的外接矩形
        self.screen_rect = screen.get_rect()  # 获取屏幕的外接矩形

        # 将飞船的位置设置在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)  # 把中心位置设置为小数并存储在一个属性变量中

        # 飞船向右移动的标志
        self.moving_right = False

        # 飞船向左移动的标志
        self.moving_left = False

    def update(self):
        """
        1.判断moving_right标志，控制飞船向右移动
        2.判断moving_left标志，控制飞船向左移动
        :return:
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.game_settings.ship_speed_factor  # 1替换为settings里面的速度设置
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.game_settings.ship_speed_factor
        self.rect.centerx = self.center  # 再把center赋给rect，更新飞船位置

    def blitme(self):
        """
        在指定位置绘制飞船
        :return:
        """
        self.screen.blit(self.image, self.rect)






#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import pygame


def check_events(ship):
    """
    事件管理，捕获键盘和鼠标事件
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 检测KEYDOWN事件，如果是右箭头键，则飞船右移
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True  # 设置向右移动的标志为True
                # ship.rect.centerx += 1

        # 检测键盘松开事件
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen(game_settings, screen, ship):
    """

    :param game_settings:
    :param screen:
    :param ship:
    :return:
    """
    # 设置屏幕背景色
    screen.fill(game_settings.bg_color)

    # 指定飞船在屏幕的位置
    ship.blitme()

    # 刷新屏幕
    pygame.display.flip()




#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import pygame


def check_keydown_events(ship, event):
    """
    检测按下键盘事件
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True  # 设置向右移动的标志为True
        # ship.rect.centerx += 1
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  # 设置向左移动的标志位True


def check_keyup_events(event, ship):
    """
    检测松开键盘事件
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


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
            check_keydown_events(event, ship)

        # 检测键盘松开事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


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




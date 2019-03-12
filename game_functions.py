#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import pygame
from bullet import Bullet


def check_keydown_events(ship, event, screen, game_settings, bullets):
    """
    检测按下键盘事件
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True  # 设置向右移动的标志为True
        # ship.rect.centerx += 1
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  # 设置向左移动的标志位True

    # 判断如果按下的是空格键，则发射子弹
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, game_settings, ship)  # 实例化一个子弹对象
        bullets.add(new_bullet)  # 将新创建的子弹添加到子弹列表中


def check_keyup_events(event, ship):
    """
    检测松开键盘事件
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(screen, game_settings, ship, bullets):
    """
    事件管理，捕获键盘和鼠标事件
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 检测KEYDOWN事件，如果是右箭头键，则飞船右移
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, game_settings, ship, bullets)

        # 检测键盘松开事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, ship, bullets):
    """

    :param game_settings:
    :param screen:
    :param ship:
    :param bullets:
    :return:
    """
    # 设置屏幕背景色
    screen.fill(game_settings.bg_color)

    # 指定飞船在屏幕的位置
    ship.blitme()

    # 在屏幕上绘制子弹
    for bullet in bullets.sprites():  # 遍历在列表里的子弹
        bullet.draw_bullet()

    # 刷新屏幕
    pygame.display.flip()




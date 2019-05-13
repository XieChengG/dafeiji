#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """
    1.初始化游戏，并创建一个屏幕，循环每次刷新屏幕最新
    2.捕获键盘和鼠标事件
    3.设置背景色
    4.设置游戏的标题
    5.创建一艘飞船，并指定其在屏幕的位置
    :return:
    """
    pygame.init()
    pygame.display.set_caption('Alien Invasion')
    game_settings = Settings()  # 实例化Settings类
    screen = pygame.display.set_mode((
        game_settings.screen_width, game_settings.screen_height))
    ship = Ship(game_settings, screen)  # 实例化Ship类,创建一艘飞船
    bullets = Group()  # 实例化编组
    aliens = Group()  # 创建用于存储外星人群的编组

    while True:
        gf.check_events(screen, game_settings, ship, bullets)
        ship.update()  # 更新飞船的位置
        gf.update_bullets(game_settings, screen, aliens, ship, bullets)  # 更新子弹
        gf.create_fleet(game_settings, screen, aliens, ship)  # 在屏幕上绘制外星人群
        gf.update_aliens(ship, aliens, game_settings)
        gf.update_screen(game_settings, screen, ship, bullets, aliens)
run_game()







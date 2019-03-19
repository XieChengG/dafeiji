#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien


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
    alien = Alien(screen, game_settings)  # 创建一个外星人实例

    while True:
        gf.check_events(ship, screen, game_settings, bullets)
        ship.update()  # 更新飞船的位置
        gf.update_bullets(bullets)  # 更新子弹
        gf.update_screen(game_settings, screen, ship, bullets, alien)
run_game()







#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import pygame
from settings import Settings

def run_game():
    '''
    1.初始化游戏，并创建一个屏幕，循环每次刷新屏幕最新
    2.捕获键盘和鼠标事件
    3.设置背景色
    4.设置游戏的标题
    :return:
    '''
    pygame.init()
    pygame.display.set_caption('Alien Invasion')
    game_settings = Settings()  # 实例化Settings类
    screen = pygame.display.set_mode((
        game_settings.screen_width, game_settings.screen_height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(game_settings.bg_color)
        pygame.display.flip()
run_game()










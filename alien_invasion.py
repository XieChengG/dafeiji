#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import pygame

def run_game():

    # 初始化游戏
    pygame.init()

    # 创建一个游戏屏幕，并设置大小
    screen = pygame.display.set_mode((1000, 600))

    # 设置游戏的标题
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)  # 设置背景颜色

    while True:

        for event in pygame.event.get():  # 获取鼠标和键盘的事件
            if event.type == pygame.QUIT:  # 捕捉用户退出事件
                sys.exit()
        screen.fill(bg_color)  # 填充颜色

        pygame.display.flip()  # 刷新屏幕，使处于最新

run_game()











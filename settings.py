#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Settings(object):
    """
    用于存储游戏的所有的设置
    """
    def __init__(self):
        self.screen_width = 1000  # 屏幕的宽度
        self.screen_height = 600  # 屏幕的高度
        self.bg_color = (230, 230, 230)  # 屏幕的背景色
        self.ship_speed_factor = 1.5  # 飞船的移动单位距离1.5像素

        # 子弹bullet类需要使用的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)







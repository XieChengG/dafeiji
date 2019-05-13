#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import pygame
from bullet import Bullet
from alien import Alien


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
        fire_bullets(game_settings, screen, ship, bullets)

    # 判断如果按下的是Q键，则退出游戏
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullets(game_settings, screen, ship, bullets):
    """发射子弹函数"""
    if len(bullets) < game_settings.bullets_allowed:  # 判断子弹列表里的子弹数量
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
            check_keydown_events(ship, event, screen, game_settings, bullets)

        # 检测键盘松开事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, ship, bullets, aliens):
    """

    :param game_settings:
    :param screen:
    :param ship:
    :param bullets:
    :param aliens:
    :return:
    """
    # 设置屏幕背景色
    screen.fill(game_settings.bg_color)

    # 指定飞船在屏幕的位置
    ship.blitme()

    # 在屏幕上绘制子弹
    for bullet in bullets.sprites():  # 遍历在列表里的子弹
        bullet.draw_bullet()

    # 在屏幕上绘制外星人群
    aliens.draw(screen)

    # 刷新屏幕
    pygame.display.flip()


def update_bullets(game_settings, screen, aliens, ship, bullets):
    bullets.update()  # 更新子弹的位置
    check_bullet_alien_collisions(game_settings, screen, aliens, ship, bullets)  # 调用函数

    # 删除已消失的子弹
    for bullet in bullets.copy():  
        if bullet.rect.bottom <= 0:  # 当子弹穿过屏幕顶端时删除
            bullets.remove(bullet)     

def check_bullet_alien_collisions(game_settings, screen, aliens, ship, bullets):
    """
    检测子弹和外星人的碰撞，发生时同时删除子弹和外星人
    当外星人消灭干净时，则生成新的外星人群
    """
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)
    
    if len(aliens) == 0:
        bullets.empty()  # 清空子弹
        create_fleet(game_settings, screen, aliens, ship)

def get_number_alien_x(game_settings, alien_width):
    """获取可用空间内一行可容纳的外星人数量"""
    available_space_x = game_settings.screen_width - 2 * alien_width  # 获取除去边距，可用的行宽度
    number_alien_x = int(available_space_x / (2 * alien_width))  # 可用空间内一行可容纳的外星人数量
    return number_alien_x


def get_number_rows(game_settings, alien_height, ship_height):
    """计算在可用的垂直空间内能
    能容纳多少行外星人"""
    available_space_y = (game_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))  # 计算能容纳外星人的行数
    return number_rows


def create_aliens(screen, game_settings, aliens, alien_number, row_number):
    """创建一个外星人，并放在当前行"""
    alien = Alien(screen, game_settings)  # 创建一个外星人实例
    alien_width = alien.rect.width  # 获取一个外星人的宽度
    alien_height = alien.rect.height  # 获取一个外星人的高度
    alien_x = alien_width + 2 * alien_width * alien_number  # 计算新创建的外星人的x坐标
    alien_y = alien_height + 2 * alien_height * row_number  # 计算新创建的外星人的y坐标
    alien.rect.x = alien_x
    alien.rect.y = alien_y
    aliens.add(alien)  # 将新创建的外星人添加到编组中


def create_fleet(game_settings, screen, aliens, ship):
    """创建外星人群"""
    alien = Alien(screen, game_settings)
    alien_width = alien.rect.width
    number_alien_x = get_number_alien_x(game_settings, alien_width)  # 计算一行外星人的个数
    number_rows = get_number_rows(game_settings, alien.rect.height, ship.rect.height)  # 获取能容纳外星人的行数

    # 创建多行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_aliens(screen, game_settings, aliens, alien_number, row_number)


def check_fleet_edges(aliens, game_settings):
    """当有外星人到达屏幕边缘时，执行动作"""
    for alien in aliens.sprites():
        if alien.check_edges:  # 获取函数check_edges的返回值为真
            change_fleet_direction(aliens, game_settings)
            break


def change_fleet_direction(aliens, game_settings):
    """外星人下移，并改变外星人的移动方向"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed  # 下移
    game_settings.fleet_direction *= -1  # 向反方向移动


def update_aliens(aliens, game_settings):
    """更新编组内的所有外星人的位置"""
    check_fleet_edges(aliens, game_settings)  # 检查是否有外星人位于屏幕边缘
    aliens.update()











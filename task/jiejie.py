import os
import sys
import random
import time
import gevent
import win32gui

from util import WindowCapture
from util.MatchImg import matchImg
from util.Cursor import click_it
from task.public import public

def click_random(point, hwnd):
    """传入点击坐标 进行随机点击"""
    rect = win32gui.GetWindowRect(hwnd)
    x = int(rect[0] + point["result"][0] - (random.randint(1, 3) * 2))
    y = int(rect[1] + point["result"][1] - (random.randint(1, 3) * 2))
    click_it((x, y), hwnd)

def jiejie(hwnd):
    print("是否在完成所有突破时候自动刷新继续？")
    auto_refresh = input("Y/N？：").lower()

    if auto_refresh == "y" or auto_refresh == "yes":
        auto_refresh = True
    elif auto_refresh == 'n' or auto_refresh == 'no':
        auto_refresh = False
    else:
        auto_refresh = False

    print(f"=== 开始进行结界突破 ===")
    fun_name = sys._getframe().f_code.co_name   # 获取当前方法名
    baseImg = f"./images/{fun_name}/"  # 储存的图片文件夹
    bg = baseImg+"background.jpg"

    stop = False
    while not stop:
        try:
            WindowCapture.window_capture(bg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
        except Exception as e:
            print(e)

        public(bg, hwnd)    # 处理公共事务

        end = matchImg(bg, baseImg+"end.png", 0.98)
        if end:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 突破卷已用完，任务执行完毕")
            stop = True

        target = matchImg(bg, baseImg+"target.png", 0.9)
        if target:
            click_random(target, hwnd)
            gevent.sleep(3)

            WindowCapture.window_capture(bg, hwnd)  # 重新截图，点击进攻按钮
            attack = matchImg(bg, baseImg+"attack.png", 0.9)
            if attack:
                click_random(attack, hwnd)
        else:
            if auto_refresh:    # 判断是否自动刷新突破
                refresh = matchImg(bg, baseImg+"refresh.png", 0.9)
                if refresh:
                    click_random(refresh, hwnd)
                    gevent.sleep(3)

                    sure = matchImg(bg, baseImg+"sure.png", 0.9)
                    if sure:
                        click_random(sure, hwnd)

        gevent.sleep(3)

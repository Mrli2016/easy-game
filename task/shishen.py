""""式神挑战（隐藏功能）"""
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

def shishen(hwnd):
    print(f"=== 开始自动使用式神挑战券 ===")
    fun_name = sys._getframe().f_code.co_name   # 获取当前方法名
    baseImg = f"./images/{fun_name}/"  # 储存的图片文件夹
    bg = baseImg+"background.jpg"

    print("请输入自动挑战的次数(默认3次)：")
    maxnum = int(input("")) or 3
    num = 0
    while num < maxnum:
        try:
            WindowCapture.window_capture(bg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
        except Exception as e:
            print(e)

        public(bg, hwnd, auto_ready=True)    # 处理公共事务

        fight = matchImg(bg, baseImg+"fight.png", 0.98)
        if fight:
            click_random(fight, hwnd)
            num += 1
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 使用第{num}张式神挑战券")

        gevent.sleep(3)

    gevent.sleep(60*30)

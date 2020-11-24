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

def summon(hwnd):
    print(f"=== 开始进行自动召唤（请进入召唤界面） ===")
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

        normal = matchImg(bg, baseImg+"normal.png", 0.9)  # 进入普通召唤
        if normal:
            click_random(normal, hwnd)
        else:
            again = matchImg(bg, baseImg+"again.png", 0.9)  # 进行再次召唤
            if again:
                click_random(again, hwnd)

        end = matchImg(bg, baseImg+"end.png", 0.98)
        if end:
            print(f"普通召唤卷已用完，任务执行完毕")
            stop = True

        gevent.sleep(3)

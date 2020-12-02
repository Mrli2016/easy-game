"""御灵"""
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

def yuhun(hwnd):
    print(f"=== 开始运行魂土自动 ===")
    fun_name = sys._getframe().f_code.co_name   # 获取当前方法名
    baseImg = f"./images/{fun_name}/"  # 储存的图片文件夹
    bg = baseImg+"background.jpg"

    while True:
        try:
            WindowCapture.window_capture(bg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
        except Exception as e:
            print(e)

        public(bg, hwnd, auto_ready=True)    # 处理公共事务

        tiaozhan = matchImg(bg, baseImg+"tiaozhan.png", 0.9) # 房主的情况下需要点击挑战
        if tiaozhan:
            click_random(tiaozhan, hwnd)

        gevent.sleep(3)

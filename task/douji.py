import os
import sys
import random
import time
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

def douji(hwnd):
    print("请输入自动斗技的场数(默认3场)：")
    maxnum = int(input("")) or 3

    print(f"=== 开始自动进行斗技({maxnum}) ===")
    fun_name = sys._getframe().f_code.co_name   # 获取当前方法名
    baseImg = f"./images/{fun_name}/"  # 储存的图片文件夹
    bg = baseImg+"background.jpg"

    num = 0
    while num < maxnum:
        try:
            WindowCapture.window_capture(bg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
        except Exception as e:
            print(e)

        public(bg, hwnd)    # 处理公共事务

        fight = matchImg(bg, baseImg+"fight.png", 0.9)
        if fight:
            click_random(fight, hwnd)
        
        shoudong = matchImg(bg, baseImg+"shoudong.png", 0.9)
        if shoudong:
            click_random(shoudong, hwnd)
        
        honor = matchImg(bg, baseImg+"honor.png", 0.9)
        if honor:
            click_random(honor, hwnd)

        ready = matchImg(bg, baseImg+"ready.png", 0.9)
        if ready:
            click_random(ready, hwnd)
            num += 1
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 开始进行第{num}场战斗")
            time.sleep(10)

        time.sleep(3)

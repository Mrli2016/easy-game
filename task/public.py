"""处理公共方法"""
import os
import sys
import random
import time
import win32gui

from util import WindowCapture
from util.MatchImg import matchImg
from util.Cursor import click_it

def click_random(point, hwnd):
    """传入点击坐标 进行随机点击"""
    rect = win32gui.GetWindowRect(hwnd)
    x = int(rect[0] + point["result"][0]+ (random.randint(1, 3) * 2))
    y = int(rect[1] + point["result"][1] + (random.randint(1, 3) * 2))
    click_it((x, y), hwnd)

def public(bg, hwnd):
    """处理公共事务，包括悬赏"""
    baseImg = f"./images/public/"  # 储存的图片文件夹

    xuanshang = matchImg(bg, baseImg+"xuanshang.png", 0.9)
    if xuanshang:
        # 出现悬赏 进行判断处理
        money = matchImg(bg, baseImg+"money.png", 0.9)
        if money:
            # 如果是勾玉悬赏，进行接受
            accept = matchImg(bg, baseImg+"accept.png", 0.9)
            if accept:
                click_random(accept, hwnd)
        else:
            refuse = matchImg(bg, baseImg+"refuse.png", 0.9)
            if refuse:
                click_random(refuse, hwnd)
    win = matchImg(bg, baseImg+"win.png", 0.9)
    if win:
        click_random(win, hwnd)
    over = matchImg(bg, baseImg+"over.png", 0.9)
    if over:
        click_random(over, hwnd)

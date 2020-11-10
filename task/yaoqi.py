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
    x = int(rect[0] + point["result"][0]+ (random.randint(1, 3) * 2))
    y = int(rect[1] + point["result"][1] + (random.randint(1, 3) * 2))
    click_it((x, y), hwnd)

def yaoqi(hwnd):
    print(f"=== 开始运行妖气封印 ===")
    fun_name = sys._getframe().f_code.co_name   # 获取当前方法名
    baseImg = f"./images/{fun_name}/"  # 储存的图片文件夹
    bg = baseImg+"background.jpg"

    num = 1
    star_time = int(time.time())
    while True:
        try:
            WindowCapture.window_capture(bg, hwnd)  # 对整个屏幕截图，并保存截图为baseImg
        except Exception as e:
            print(e)

        public(bg, hwnd)    # 处理公共事务

        finding = matchImg(bg, baseImg+"finding.png", 0.9)
        if not finding:
            # 如果不是匹配中则进行组队匹配
            zudui = matchImg(bg, baseImg+"zudui.png", 0.9)
            if zudui:
                click_random(zudui, hwnd)
            pipei = matchImg(bg, baseImg+"pipei.png", 0.9)
            if pipei:
                star_time = int(time.time())
                click_random(pipei, hwnd)
            ready = matchImg(bg, baseImg+"ready.png", 0.8)
            if ready:
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 妖气封印开始第{num}次战斗 等待了：{(int(time.time()) - star_time)/60}分钟")
                click_random(ready, hwnd)
                num += 1
                time.sleep(20)
        # 失败
        # fail = matchImg(bg, baseImg+"fail.png", 0.9)
        # if fail:
        #     print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 战斗失败")
        #     click_random(fail, hwnd)
        time.sleep(3)

# -*- coding: utf-8 -*
import logging
import os

from util.Cursor import my_sleep
from util.game_ctl import GameControl

logging.basicConfig(format='%(asctime)s - %(levelname)s： %(message)s', datefmt='%H:%M:%S', level="DEBUG")


class Robot(GameControl):

    def __init__(self, hwnd=0, tpl_dir=None, interval=1000, auto_ready=True, task_name=""):
        """"
        初始化
        """
        GameControl.__init__(self, hwnd=hwnd)
        self.yys = GameControl(hwnd)    # 窗口句柄
        self.logging = logging

        self.task_name = task_name
        self.interval = interval
        self.tpl_dir = os.path.join(os.getcwd(), "images", tpl_dir)    # 待识别的模板图片文件夹
        print(self.tpl_dir)
        self.auto_ready = auto_ready            # 是否自动准备
        self.bg = None                          # 截取的图片背景

        self.stop = False

        # 激活窗口
        self.yys.activate_window()

    def start_log(self):
        """
        启动信息
        """
        logging.info(self.task_name + '任务开始运行')

    def pre_start(self):
        """开始前的钩子"""
        pass

    def start(self):
        self.pre_start()
        """开始循环执行识别任务"""
        while not self.stop:
            self.update_bg()
            self.public_task(auto_ready=self.auto_ready)
            self.runner()
            my_sleep(self.interval)

    def runner(self):
        """
        具体判断逻辑
        """
        pass

    def take_stop(self):
        """停止运行"""
        self.stop = True

    def update_bg(self):
        """更新背景截图"""
        self.bg = self.window_full_shot()

    def find_and_click(self, img_path=None):
        """
        查找图片是否存在，存在的话进行点击
        :param img_path:
        :return:
        """
        if img_path is None:
            return False

        target = self.find_img_knn(img_path)  # 图片目标
        if target:
            self.yys.mouse_click_bg(target)
            return True
        return False

    def save_bg(self):
        self.window_full_shot(os.path.join(self.tpl_dir, "bg.png"))
"""
自动斗技
"""
import os

from task.AutoRobot import Robot
from util.Cursor import my_sleep
from util.tools import PublicPos


class DouJi(Robot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_name = "自动斗技"
        self.douji_num = 0
        self.douji_max_num = 5

    def pre_start(self):
        # self.window_full_shot("F:/code/yys2/images/bg.png")
        print("输入自动斗技次数？")
        self.douji_max_num = int(input("次数：")) or 5

        self.logging.info(f"开始进行自动打斗技")

    def runner(self):
        if self.douji_num > self.douji_max_num:
            self.logging.info("自动斗技任务执行完毕")
            self.take_stop()
            my_sleep(3000)
            return

        self.find_and_click(os.path.join(self.tpl_dir, "fight.png"))     # 选择突破目标
        self.find_and_click(os.path.join(self.tpl_dir, "shoudong.png"))
        self.find_and_click(os.path.join(self.tpl_dir, "honor.png"))
        self.find_and_click(os.path.join(self.tpl_dir, "ready.png"))

        ready = self.find_img_knn(os.path.join(self.tpl_dir, "ready.png"))
        if ready:
            self.yys.mouse_click_bg(*PublicPos.ready_btn)
            self.douji_num += 1
            self.logging.info(f"开始进行第{num}场斗技战斗")


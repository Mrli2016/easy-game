"""
寮宴
"""
import os

from task.AutoRobot import Robot
import os
from util.tools import YuhunPos


class LiaoYan(Robot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_name = "自动寮宴"

    def pre_start(self):
        self.logging.info(f"开始进行自动寮宴！")

    def runner(self):
        self.find_and_click(os.path.join(os.path.join(self.tpl_dir, "num1.png")))
        self.find_and_click(os.path.join(os.path.join(self.tpl_dir, "num2.png")))
        self.find_and_click(os.path.join(os.path.join(self.tpl_dir, "num3.png")))
        self.find_and_click(os.path.join(os.path.join(self.tpl_dir, "jingyan.png")))
        self.find_and_click(os.path.join(os.path.join(self.tpl_dir, "baozhu.png")))

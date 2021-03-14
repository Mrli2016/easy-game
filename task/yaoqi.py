"""
妖气封印
"""
import os
import time

from task.AutoRobot import Robot
from util.time_tools import subtime


class YaoQi(Robot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_name = "妖气封印"
        self.yaoqi_star_time = int(time.time())
        self.yaoqi_num = 0

    def pre_start(self):
        self.yaoqi_star_time = int(time.time())
        self.yaoqi_num = 0

        self.logging.info(f"开始进行自动排队妖气封印！")

    def runner(self):
        target = self.find_img_knn(os.path.join(self.tpl_dir, "finding.png"))
        if not target:
            # 如果不是匹配中则进行组队匹配
            target = self.find_img_knn(os.path.join(self.tpl_dir, "zudui.png"))
            if target:
                self.yys.mouse_click_bg(target)
                return
            target = self.find_img_knn(os.path.join(self.tpl_dir, "pipei.png"))
            if target:
                self.yaoqi_star_time = time.time()
                self.yys.mouse_click_bg(target)
                return
            target = self.find_img_knn(os.path.join(self.tpl_dir, "start.png"))
            if target:
                # 房主的情况下需要点击挑战
                self.yys.mouse_click_bg(target)
                return
            target = self.find_img_knn(os.path.join(self.tpl_dir, "ready.png"))
            if target:
                self.yaoqi_num += 1
                self.logging.info(f"妖气封印开始第{self.yaoqi_num}次战斗 排队等待了：{subtime(time.time(), self.yaoqi_star_time)}")

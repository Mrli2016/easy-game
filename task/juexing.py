""""自动觉醒"""
import os

from task.AutoRobot import Robot
from util.tools import YuhunPos


class JueXing(Robot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_name = "自动觉醒"

    def pre_start(self):
        self.logging.info(f"开始进行自动觉醒！")

    def runner(self):
        fight = self.find_img_knn(os.path.join(self.tpl_dir, "fight.png"))  # 房主的情况下需要点击挑战
        if fight:
            self.yys.mouse_click_bg(*YuhunPos.fight_btn)

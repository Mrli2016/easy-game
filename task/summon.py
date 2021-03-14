""""厕纸召唤"""
import os

from task.AutoRobot import Robot
from util.tools import YuhunPos


class Summon(Robot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_name = "厕纸召唤"

    def pre_start(self):
        self.logging.info(f"开始进行自动召唤！")

    def runner(self):
        normal = self.find_img_knn(os.path.join(self.tpl_dir, "normal.png"))  # 房主的情况下需要点击挑战
        if normal:
            self.yys.mouse_click_bg(*YuhunPos.fight_btn)
        else:
            self.find_and_click(os.path.join(self.tpl_dir, "again.png"))

        end = self.find_img_knn(os.path.join(self.tpl_dir, "end.png"), 0.98)  # 房主的情况下需要点击挑战
        if end:
            self.logging.info("普通召唤卷已用完，任务执行完毕")
            self.take_stop()

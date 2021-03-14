""""自动寮突破"""
import os

from task.AutoRobot import Robot
from util.Cursor import my_sleep


class LiaoTuPo(Robot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_name = "自动寮破"

    def pre_start(self):
        self.logging.info(f"开始进行自动寮突破跟助威！")

    def runner(self):
        if self.find_and_click(os.path.join(self.tpl_dir, "fight.png")):
            return

        watch = self.find_img_knn(os.path.join(self.tpl_dir, "watch.png"))  # 房主的情况下需要点击挑战
        if watch:
            self.yys.mouse_click_bg(watch)
            my_sleep(2)
            self.update_bg()
            if self.find_and_click(os.path.join(self.tpl_dir, "to_watch.png")):
                return

        if self.find_and_click(os.path.join(self.tpl_dir, "to_watch.png")):
            return


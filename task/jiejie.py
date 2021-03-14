"""
结界突破
"""
import os

from task.AutoRobot import Robot
from util.Cursor import my_sleep


class Jiejie(Robot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_name = "结界突破"
        self.auto_refresh = False

    def pre_start(self):
        print("是否在完成所有突破时候自动刷新继续？")
        auto_refresh = input("Y/N？：").lower()

        if auto_refresh == "y" or auto_refresh == "yes":
            self.auto_refresh = True
        self.logging.info(f"开始进行自动突破！{'(自动刷新突破结界)' if self.auto_refresh else ''}")

    def runner(self):
        end = self.find_img_knn(os.path.join(self.tpl_dir, "end.png"), threshold=0.98)
        if end:
            self.logging.info("突破卷已用完，任务执行完毕")
            self.take_stop()
            my_sleep(3000)
            return

        target = self.find_img_knn(os.path.join(self.tpl_dir, "target.png"))     # 选择突破目标
        if target:
            self.yys.mouse_click_bg(target)
            my_sleep(1000)

            self.update_bg()
            attack = self.find_img_knn(os.path.join(self.tpl_dir, "attack.png"))
            if attack:
                self.yys.mouse_click_bg(attack)
                return
        else:   # 没有突破目标的时候进行判断是否自动刷新突破
            if self.auto_refresh:  # 判断是否自动刷新突破
                refresh = self.find_img_knn(os.path.join(self.tpl_dir, "refresh.png"))
                if refresh:
                    self.yys.mouse_click_bg(refresh)
                else:
                    sure = self.find_img_knn(os.path.join(self.tpl_dir, "sure.png"))
                    if sure:
                        self.yys.mouse_click_bg(sure)

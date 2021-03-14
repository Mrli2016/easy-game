"""
御魂
"""
import os

from task.AutoRobot import Robot
from util.tools import YuhunPos


class Yuhun(Robot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task_name = "自动御魂"
        self.yuhun_single_mode = False
        self.yuhun_fight_btn = "fight.png"

    def pre_start(self):
        print("是否单人模式刷御魂？")
        answer = input("Y/N？：").lower()

        if answer == "y" or answer == "yes":
            self.yuhun_single_mode = True
            self.yuhun_fight_btn = "single_fight.png"
        self.logging.info(f"开始进行自动御魂！{'(个人模式)' if self.yuhun_single_mode else '（多人模式）'}")

    def runner(self):
        fight = self.find_img_knn(os.path.join(self.tpl_dir, self.yuhun_fight_btn))  # 房主的情况下需要点击挑战
        if fight:
            self.yys.mouse_click_bg(*YuhunPos.fight_btn)

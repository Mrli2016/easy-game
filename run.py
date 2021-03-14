import time

from task.douji import DouJi
from task.juexing import JueXing
from task.liaotupo import LiaoTuPo
from task.liaoyan import LiaoYan
from task.summon import Summon
from task.yaoqi import YaoQi
from task.yuhun import Yuhun
from task.jiejie import Jiejie

from util.HwndList import get


def main():
    # 获取所有阴阳师句柄
    hd_list = get()
    hd_len = len(hd_list)

    if hd_len == 0:
        print("未发现阴阳师窗口！")
        raise SystemExit
    elif hd_len == 1:
        target_hd = hd_list[0]
    else:
        for inx, hd in enumerate(hd_list):
            print(f'窗口{inx + 1}: {hd}')

        num = int(input(f'当前有{hd_len}个阴阳师窗口，请选择要运行的窗口：') or 1) - 1
        if not hd_list[num]:
            print('窗口选择失败，请重新运行')
            time.sleep(3000)
            raise SystemExit
        target_hd = hd_list[num]

    print('当前运行的阴阳师窗口：', target_hd)
    print('选择运行脚本类型：')
    task_list = [
        {'name': "自动御魂", 'cls': Yuhun, "tpl_dir": "yuhun"},
        {"name": "自动斗技", 'cls': DouJi, "tpl_dir": "douji"},
        {"name": "自动觉醒", "cls": JueXing, "tpl_dir": "juexing"},
        {"name": "结界突破", 'cls': Jiejie, "tpl_dir": "jiejie"},
        {"name": "妖气封印", 'cls': YaoQi, "tpl_dir": "yaoqi"},
        {"name": "自动寮破", 'cls': LiaoTuPo, "tpl_dir": "liaotupo"},
        {"name": "自动寮宴", 'cls': LiaoYan, "tpl_dir": "liaoyan"},
        {"name": "厕纸召唤", 'cls': Summon, "tpl_dir": "summon"},
    ]
    for inx, task in enumerate(task_list):
        print(f"{inx + 1}、{task.get('name')}")
    try:
        task_num = int(input("输入任务类型：") or 1) - 1
    except ValueError:
        task_num = 0

    task = task_list[task_num]
    task_cls = task.get("cls")
    func = task_cls(hwnd=target_hd, task_name=task.get("name"), tpl_dir=task.get("tpl_dir"))
    func.start()


if __name__ == "__main__":
    main()

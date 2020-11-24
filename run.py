import sys
import time
import gevent

from util.HwndList import get

def main():
    print("欢迎来到阴阳师联盟！")

    #  X = 1009.0
    # global Y = 604.0

    arg = 0
    tt = 5
    if sys.argv.__len__() > 1:  #多人组队
        arg = sys.argv[1]
    else:
        tt = 1
    #获取所有阴阳师句柄
    hd_list = get()
    hd_len = len(hd_list)
    target_hd = hd_list[0]
    if hd_len > 1:
        print(f'当前有{hd_len}个阴阳师窗口，请选择要运行的窗口：')
        for inx, hd in enumerate(hd_list):
            print(f'{inx+1}: {hd}')

        num = int(input("")) - 1
        if not hd_list[num]:
            print('窗口选择失败，请重新选择')
            raise SystemExit
        target_hd = hd_list[num]
    
        
    print('当前运行的阴阳师窗口：', target_hd)
    print('选择运行脚本类型：')
    task_list = ['妖气封印', '结界突破', '厕纸自动召唤', '自动斗技', '寮突破']

    for inx, name in enumerate(task_list):
        print(f"{inx+1}、{name}")

    task_num = int(input("输入任务类型：")) - 1

    fun = None
    if task_num == 0:
        # 自动妖气封印
        from task.yaoqi import yaoqi
        fun = yaoqi
    elif task_num == 1:
        # 自动结界突破
        from task.jiejie import jiejie
        fun = jiejie
    elif task_num == 2:
        # 厕纸自动召唤
        from task.summon import summon
        fun = summon
    elif task_num == 3:
        # 自动斗技
        from task.douji import douji
        fun = douji
    elif task_num == 4:
        # 自动寮突破
        from task.liaotupo import liaotupo
        fun = liaotupo
    elif task_num == 5:
        # 自动御灵
        from task.yuling import yuling
        fun = yuling
    elif task_num == 8:
        from task.shishen import shishen
        fun = shishen
    
    if fun:
        gevent.joinall([  # 利用joinall方法将每一步操作加入协程池中
            gevent.spawn(fun, target_hd)
        ])

if __name__=="__main__":
    main()







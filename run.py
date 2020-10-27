import sys
import time

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
        

    print('选择运行脚本类型：')
    task_list = ['妖气封印']

    for inx, name in enumerate(task_list):
        print(f"{inx+1}、{name}")

    task_num = int(input("输入任务类型：")) - 1

    if task_num == 0:
        from task.yaoqi import yaoqi
        yaoqi(target_hd)

    # while True:
    #     time.sleep(tt)  # 设置隔2秒运行一次

        #循环所有句柄

if __name__=="__main__":
    main()







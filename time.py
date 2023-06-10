import time
import os

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

# 设置专注时间（默认为25分钟）和休息时间（默认为5分钟）
focus_time = 25 * 60
break_time = 5 * 60

while True:
    # 专注
    os.system('clear')
    print("开始专注时间\n")
    countdown(focus_time)

    # 休息
    os.system('clear')
    print("休息时间！\n")
    countdown(break_time)

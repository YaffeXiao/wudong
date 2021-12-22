from core.PlayerAasync import Player
from sys import argv
import threading
from pynput.keyboard import Key, Listener
import sys


def on_press(key):
    pass


def on_release(key):
    if key == Key.esc:
        # 停止监听
        Player.STOP_PROGRAM = True
        return False


# 开始监听
def start_listen():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    t1 = threading.Thread(target=start_listen, args=())
    t1.start()
    print("按ESC退出程序")
    p = None
    if len(argv) > 2:
        p = Player(argv[2])
    else:
        p = Player()
    # p = Player("debug")
    # p = Player("on")
    p.start_play()

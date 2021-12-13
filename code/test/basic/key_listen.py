import sys

from pynput.keyboard import Key, Controller, Listener
keyboard = Controller()


def on_press(key):
    print('{0} 被按下'.format(key)) 


def on_release(key):
    print('{0} 被释放'.format(key))
    if key == Key.esc:
        return False
    if str(key) == r"<48>":# ctrl 0
        tt()


def tt():
    print('按下ctrl 0,运行测试程序')
    sys.exit(0)


# 创建监听
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

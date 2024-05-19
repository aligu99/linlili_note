import random
import time
import pyautogu._pyautogui_win as platformModule


def real_press(key):
    platformModule._keyDown(key)
    time.sleep(random.uniform(0.05, 0.1))
    platformModule._keyUp(key)


def real_write(s):
    for c in s:
        real_press(c)
    time.sleep(random.uniform(0.04, 0.06))


for _ in range(20):
    for _ in range(45):
        real_write('zhany ')
        time.sleep(random.uniform(0.05, 0.09))
    real_write('\n')
    time.sleep(random.uniform(0.05, 0.09))

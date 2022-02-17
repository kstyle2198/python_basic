import pyautogui as gui
import time


# gui.moveTo(500, 500, 3)
# print("작업1")
# a = gui.locateOnScreen('./images/target.png')
# print(f"{a[0]}, {a[1]}")
# x, y = a[0]+10, a[1]+10
# print(f"{x}, {y}")

# gui.moveTo(x, y)

# gui.moveTo(gui.locateCenterOnScreen('./images/target.png'))
# gui.moveTo(gui.locateCenterOnScreen('./images/angle.png'))


# 화면에서 동일한 이미지를 전부 찾아내기

result = list(gui.locateAllOnScreen('./images/target.png'))
print(result)
print(len(result))
gui.moveTo(1, 1)
gui.dragTo(1, 1, 0.5, button='left')

for pos in result:

    x, y = pos[0]+20, pos[1]+10
    time.sleep(1)
    gui.moveTo(x, y, 1, gui.easeInOutQuad)
    time.sleep(0.1)
    gui.dragTo(x+200, y, 1, button='left')
    time.sleep(2)
    print("다음")


print("작업완료")

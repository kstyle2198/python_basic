import pyautogui as gui
import time
from slack import *


# 계속 진행여부 체크 함수
def go_or_stop(n):
    go_check = gui.confirm(
        text="계속진행하시겠습니까?", title="진행여부 체크", buttons=("Go", "Stop"))
    if go_check == "Stop":
        print(f"{n}번 작업중지")
        quit()
    else:
        print(f"{n}번 작업후 계속 진행")
        pass

# gui.moveTo(500, 500, 3)
# print("작업1")
# a = gui.locateOnScreen('./images/check_box.png')
# print(f"{a[0]}, {a[1]}")
# gui.moveTo(a[0], a[1])
# x, y = a[0]+10, a[1]+10
# print(f"{x}, {y}")

# gui.moveTo(x, y)


# gui.moveTo(gui.locateCenterOnScreen('./images/angle.png'))


# 화면에서 여러개의 동일한 이미지를 전부 찾아내서 왼쪽으로 드래그해서 옮기기
# result = list(gui.locateAllOnScreen('./images/target.png'))
# print(result)
# print(len(result))
# gui.moveTo(1, 1)
# gui.dragTo(1, 1, 0.5, button='left')

# for pos in result:
#     x, y = pos[0]+20, pos[1]+10
#     time.sleep(1)
#     gui.moveTo(x, y, 1, gui.easeInOutQuad)
#     time.sleep(0.1)
#     gui.dragTo(x+200, y, 1, button='left')
#     time.sleep(2)
#     print("다음")

# print("작업완료")


# 좌상단 체크박스부터 순차적으로 체크하면서 작업 수행하기
chk_boxs = list(gui.locateAllOnScreen('./images/check_box.png'))
print(f"총 작업대상 개수는 {len(chk_boxs)}개 입니다.")
gui.moveTo(500, 500)
gui.click()
print("작업개시")
time.sleep(2)
n = 1
for i in chk_boxs:
    gui.moveTo(gui.locateCenterOnScreen('./images/check_box.png'))
    time.sleep(0.1)
    gui.click()
    time.sleep(0.1)
    go_or_stop(n)
    n += 1

print("작업종료")
Slack_Msg("작업이 정상적으로 종료되었습니다.")

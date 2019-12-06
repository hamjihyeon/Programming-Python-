import pyautogui as pag
import time

if __name__ == '__main__':
    # while True:
    #     x, y = pag.position() #좌표 구하기
    #     print("x: {}\ty: {}".format(x, y),end="\r")
    # pag.moveTo(484, 44, duration=2)   #-까지 이동
    # pag.move(100,200, duration=2) #-만큼 이동
    # pag.click()
    # pag.click()http://ticket.interpark.com/

    # pag.doubleClick() #더블클릭
    # pag.click(clicks=2)   #더블클릭

    # pag.drag(0,200, duration=1)   #드래그 duration있어야 함

    # pag.rightClick()  #오른쪽버튼

    # pag.click(484, 44, duration=2)

    # pag.doubleClick(484, 44, duration=2)

    #인터파크 들어가기
    # time.sleep(1)   #크롬이 열리기를 기다려야만 함
    # pag.typewrite("http://ticket.interpark.com/")
    # pag.press("enter")

    #아이유 한글키 먹기
    # pag.press("hangul")
    # pag.typewrite("dkdldb")   #아이유 영어로
    # pag.press("enter")

    #ToDo: scroll
    pag.hotkey("alt", "tab")
    time.sleep(2)
    # pag.scroll(clicks = -2000, x = 798 , y = 185)

    pag.scroll(-2000, 789, 185)


import pyautogui as pag

if __name__ == '__main__':
    #메모장 프로그램 실행하자
    pag.press("winleft")
    pag.press("hangul")
    pag.typewrite("apah")
    pag.press("enter")

    pag.sleep(1)
    #hello_world 치자
    pag.typewrite("Hello world")

    #두 줄 내리자
    pag.press("enter",2)
    #반갑구나 세상아 치자
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")


    #hello_world 저장하자
    pag.hotkey("ctrl", "s")
    pag.press("hangul")
    pag.typewrite("Hello World")
    pag.sleep(1)
    pag.press("enter")
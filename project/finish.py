from tkinter import *
import tkinter as tk



class finish:
    def __init__(self): # button을 누르면 종료시키는 함수
        self.window = tk.Toplevel()
        img = PhotoImage(file="쿠키런.gif")
        label = Label(self.window, image=img)


        label.pack()
        btn = tk.Button(self.window, text="결과보기는 다음에 이용해주세욤", font=("배달의민족 주아", 15),command = quit).pack()



        self.window.mainloop()



if __name__ == '__main__':
    finish = finish()
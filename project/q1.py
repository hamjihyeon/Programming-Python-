from tkinter import *
import tkinter as tk

import pymysql
from q2 import *
from project import q2


class q1:
    def __init__(self,name):    #문제를 푸는 함수
        self.window = tk.Toplevel()
        image = PhotoImage(file="공주맛쿠키.png")
        label = Label(self.window, image=image)
        var = IntVar()
        R1 = Radiobutton(self.window, text="공주맛쿠키", value=1, variable =var)
        R2 = Radiobutton(self.window, text="프린세스맛쿠키", value=2, variable =var)
        btn = tk.Button(self.window, text="다음", font=("배달의민족 주아", 15), command=lambda:self.update(var.get(),name))
        label.pack()
        R1.pack()
        R2.pack()
        btn.pack()
        self.window.mainloop()


    def update(self, R2,name):  # db에 답을 update시키는 함수
        if R2 == 1:
            conn = pymysql.connect(host='127.0.0.1', user='root', password='mirim2',
                                   db='javap', charset='utf8')
            try:
                with conn.cursor() as cursor:
                    sql = "update pypeople set answer=answer+1 where person=%s" # answer 기본값이 0이고, 만약 정답이 아니면 +1을 해주지 않는다.
                    cursor.execute(sql,name)
                conn.commit()
            finally:
                conn.close()
        q2.q2(name)


if __name__ == '__main__':
    q1 = q1(name)
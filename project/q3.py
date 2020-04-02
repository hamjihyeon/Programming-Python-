from tkinter import *
import tkinter as tk

import pymysql
from q4 import *
from project import q4


class q3:
    def __init__(self,name):
        self.window = tk.Toplevel()
        image = PhotoImage(file="의적맛쿠키.png")
        label = Label(self.window, image=image)
        var = IntVar()

        R1 = Radiobutton(self.window, text="홍길동맛쿠키", value=5, variable =var)
        R2 = Radiobutton(self.window, text="의적맛쿠키", value=6, variable =var)

        btn = tk.Button(self.window, text="다음", font=("배달의민족 주아", 15), command=lambda:self.update(var.get(),name))

        label.pack()
        R1.pack()
        R2.pack()
        btn.pack()
        self.window.mainloop()
    def update(self, R2,name):
        if R2==6:
            conn = pymysql.connect(host='127.0.0.1', user='root', password='mirim2',
                                   db='javap', charset='utf8')
            try:
                with conn.cursor() as cursor:
                    sql = "update pypeople set answer=answer+1 where person = %s"
                    cursor.execute(sql,name)
                conn.commit()
            finally:
                conn.close()
        q4.q4(name)


if __name__ == '__main__':
    q3 = q3(name)
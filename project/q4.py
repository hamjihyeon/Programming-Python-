from tkinter import *
import tkinter as tk

import pymysql
from q5 import *
from project import q5


class q4:
    def __init__(self,name):
        self.window = tk.Toplevel()
        image = PhotoImage(file="천사맛쿠키.png")
        label = Label(self.window, image=image)
        var = IntVar()
        btn = tk.Button(self.window, text="다음", font=("배달의민족 주아", 15), command=lambda:self.update(var.get(),name))

        R1 = Radiobutton(self.window, text="천사맛쿠키", value=7, variable =var)
        R2 = Radiobutton(self.window, text="엔젤맛쿠키", value=8, variable =var)
        label.pack()
        R1.pack()
        R2.pack()
        btn.pack()
        self.window.mainloop()

    def update(self, R1,name):
        if R1==7:
            conn = pymysql.connect(host='127.0.0.1', user='root', password='mirim2',
                                   db='javap', charset='utf8')
            try:
                with conn.cursor() as cursor:
                    sql = "update pypeople set answer=answer+1 where person=%s"
                    cursor.execute(sql,name)
                conn.commit()
            finally:
                conn.close()
        q5.q5(name)

if __name__ == '__main__':
    q4 = q4(name)
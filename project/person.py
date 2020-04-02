from tkinter import *
from q1 import *
import pymysql
import tkinter as tk


from project import q1


class person:
    def __init__(self): #이름을 입력하는 함수
        self.window = tk.Toplevel()

        label1 = Label(self.window, text = "이름을 입려하세요")
        img = PhotoImage(file="쿠키런.gif")
        label = Label(self.window, image=img)

        text = tk.Entry(self.window, font = ("배달의민족 주아,", 15))
        btn = tk.Button(self.window, text="다음", font=("배달의민족 주아", 15), command=lambda:self.insert(text.get()))

        label1.pack()
        label.pack()
        text.pack()
        btn.pack()
        self.window.mainloop()

    def insert(self, name): # db에 저장하는 함수
        conn = pymysql.connect(host='127.0.0.1', user='root', password='mirim2',
                               db='javap', charset='utf8')
        try:
            with conn.cursor() as cursor:
                sql = "insert into pypeople(person) values(%s)"
                cursor.execute(sql, name)
            conn.commit()

        finally:
            conn.close()
        q1.q1(name)


if __name__ == '__main__':
    person = person()


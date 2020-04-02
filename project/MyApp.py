# 2419 함지현
# 쿠키런 캐릭터에 대해 알고 싶거나, 쿠키런을 많이 한 사람들이 재미를 얻고 싶어하는 사람들을 위해 만든 프로그램이다.
# 이름을 입력하면 db에 저장이 되고, 문제를 푸는데 정답일 때마다 db에서 update를 해 나중에 맞춘 정답 수랑 이름을 보여준다.
# 프로젝트 순서 : MyApp -> person -> q1 -> q2 -> q3 -> q4 -> q5 -> finish

from tkinter import *
import tkinter as tk
from person import *
import pymysql

from project import person


class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("650x550")

        img = PhotoImage(file="쿠키런.gif")
        label = Label(self.root, image=img)
        btn = tk.Button(self.root, text = "시작하기", font = ("배달의민족 주아", 15), command = person.person) #command : 다음 클래스로 이동
        label.pack()
        btn.pack()
        self.root.mainloop()

if __name__ == '__main__':
    # db 연동
    conn = pymysql.connect(host='127.0.0.1', user='root', password='mirim2',
                           db='javap', charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = "select * from pypeople"
            cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()

    # db값 가져오기(select문)
    # 이 select문이 없다면 콘솔에 가져올 수 없다
    # fetchall은 db에 있는 모든 값을 가져올 수 있는데 result에 저장했다.
        # for문을 사용하였고 row[0], row[1]을 사용해 db에 있던 person과 answer을 가져올 수 있다.
        conn = pymysql.connect(host='127.0.0.1', user='root', password='mirim2',
                               db='javap', charset='utf8')
        try:
            with conn.cursor() as cursor:
                sql = "select * from pypeople"
                cursor.execute(sql)
                result = cursor.fetchall()
                print("지금까지 이용한 사람(5점 만점)")
                for row in result:
                    print("이름 :", row[0], "/ 맞춘 정답 수 :", row[1],"점")
            conn.commit()
        finally:
            conn.close()
    MyApp = MyApp()


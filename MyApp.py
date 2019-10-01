import tkinter

window=tkinter.Tk()

window.title("궁금해, 너의 캐릭터")
window.geometry("640x400+100+100")
window.resizable(False, False)

#레이블
label=tkinter.Label(window, text="안녕하세요.")
label.pack()

window.mainloop()
def hello(msg="안녕하세요"):
    print(msg + "!")

hello("오랫만이에요")
hello("이영희")
hello()

def hello2(name="무명", msg = "안녕하세요"):
    print(name+"님,", msg+"!")

hello2("김철수", "오랫만이에요")
hello2()
hello2("김민지")
hello2(msg="오랫만이에요")

def hello3(name, msg="안녕하세요"):
    print(name+"님", msg+"!")

hello3("김봄이", "오릿만이에요")
hello3("김소현")
# hello3()    #error name을 줘야한다.

def fn(a, b=[]):
    b.append(a)
    print(b)

fn(3)   #[3]
fn(5)   #[3, 5]
fn(10)  #[3, 5, 10]
fn(7, [1])  #[3, 5, 10, 7, 1] = X [7, 1] = 0

def gugudan(dan=2):
    for i in range(1, 9+1):
        print("{} X {} = {}".format(dan, i, dan*i))

gugudan(3)
gugudan()


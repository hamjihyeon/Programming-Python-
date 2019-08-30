def fn(a, b, c, d, e):
    print(a, b, c, d, e)

fn(1, 2, 3, 4, 5)
fn(10, 20, 30, 40, 50)
fn(5, 6, 7, 8, 9)
fn(a=1, b=2, c=3, d=4, e=5) #1 2 3 4 5
fn(e=5, d=4, c=3, b=2, a=1) #1 2 3 4 5
fn(1, 2, c=3, e=5, d=4)     #1 2 3 4 5
# fn(d=4, e=5, 1, 2, 3) 키워드 인자는 위치 인자 다음에 나와야 한다.

def fn2(a, b, c, *d):
    print(a, b, c, d)

# fn(c=3, b=2, a=1, 4, 5)     #error
# fn(1, 2, c=3, 4, 5)         #error
# fn(4, 5, a=1, b=2, c=3)       #error

#118 혼자 해 보기
def star(mark, repeat, space, space_repeat, line):
    for i in range(1, line):
        string = (mark * repeat)
        for j in range(2, repeat):
            string += (space * space_repeat) + (mark * repeat)
        print(string)

star("*", 1, "♣", 3, 5)
print("-----------------------")
star(mark="*", repeat=2, space="+", space_repeat=3, line=5)

def star2(mark, repeat, space, space_repeat, line):
    string = (mark*repeat) + (space*space_repeat) + (mark * repeat)
    for n in range(line):
        print(string)

star2("※", 3,"_", 2, 3)
print("===================")
star2(mark="※", repeat=3, space="_", space_repeat=2, line=3)


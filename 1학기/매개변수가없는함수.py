import random   #임의의 값을 얻기 위해 사용하는 random 모듈을 가져온다.

#처음 시작
def rolling_dice():
    n = random.randint(1,6)    #1에서 6까지의 정수 중에 하나를 뽑는다.
    print("6면 주사위 굴린 결과 : ", n)

rolling_dice()
rolling_dice()
rolling_dice()

#start함수 정의
def star():
    print("*****")
star()
star()
star()

def rolling_dice(pip):
    n = random.randint(1,pip)
    print(pip, "면 주사위 굴린 결가: ", n)

rolling_dice(4)
rolling_dice(5)
rolling_dice(6)

def rolling_dice(pip, repeat):
    for r in range(1, repeat + 1):
        n = random.randint(1, pip)
        print(pip,"면 주사위 굴린 결과", r, ":", n)
rolling_dice(6, 1)
rolling_dice(6, 2)
rolling_dice(12, 0)
rolling_dice(20, -3)

#가변인수
print("가변인수-------------------------")
print("♡")
print("♡", "♪")
print("♡", "♪", "♣")
print("♡", "♪", "♣", "♠")
print("♡", "♪", "♣", "♠", "★")

def p(*args):
    string = ""
    for a in args:
        string += a
    print(string)
p("♡")
p("♡", "♪")
p("♡", "♪", "♣")
p("♡", "♪", "♣", "♠")

#퀴즈
#안녕()함수를 만들고,
def 안녕(*args):
    for a in args:
        print("안녕,", a)
안녕("가연아","수빈아", "정윤아")

def p( space, space_num,  *args ):
# def p( *args, space, space_num ):    args는 앞에 사용할 수 없음
        string = args[0]
        for i in range(1, len(args)):
                string = string + (space * space_num) + args[i]
        print(string)

p(",", 3, "♡", "♪")
p(",", 3, "♡", "♪", "♣")
p(",", 3, "♡", "♪", "♣", "♠")
p(",", 3, "핱")           #핱
p(",", 3, "핱", "음")           #핱,,,습
p("별", 2, "핱", "음", "습")    #핱별별음별별습

#p115 혼자 해 보기
def star( word, *args):
        for i in args:
                print(word*i)

star("음", 3)   #음음음

star("핱", 1, 2, 3)     #핱
                        #핱핱
                        #핱핱핱
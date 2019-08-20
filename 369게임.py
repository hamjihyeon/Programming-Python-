#369 게임 (if, 글자 자르기)

print('369 GAME')

while True :
    num = int(input("~369 369 ~ 369 369 ~ : "))
    if (num%3) != 0 :
        print(num)
    else :
        print("짝~ "*num)
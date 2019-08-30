import random

num=input("우리반 아이들 중 마지막 번호는? : ")
stu_num=list(range(1,int(num)+1))
while True:
    minus_ans=input("제외할 번호를 입력하세요(없는경우 대문자 X를 입력하세요) : ")
    if minus_ans=='X':
        break
    else:
        stu_num.remove(int(minus_ans))
print("자리 학생번호")
random.shuffle(stu_num)
for i in range (0,20):
    print(i+1, stu_num[i])
    

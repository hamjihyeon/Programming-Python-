#버스 여유, 보통, 혼잡
#탑승객, 하차객 입력받자
#0명 이상 10명 미만 여유
#10명 이상 20명 미만 보통
#20명 이상 혼잡

#--------
sum = 0
while True:
    enter = input("탑승객을 입력해주세요(정류장 없으면 -1) : ")
    if enter == "-1" :
        break
    enter = int(enter)
    out = input("하차객을 입력해주세요 : ")
    out = int(out)
    sum += enter - out
#-------
print("버스의 있는 사람수는 : ", sum)
if 0 <=sum < 10:
    print("여유")
elif 10 <= sum <20:
    print("보통")
else:
    print("혼잡")
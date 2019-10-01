fi = open("history.ama", "r", encoding="utf-8")
while True:
    data = fi.readline()
    if not data:
        break
    print(data, end = "")
    # 한줄 안에서 이름 가격 ... 자르기
    # 총금액 계산하고 출력하기

fi.close()

#print(data)
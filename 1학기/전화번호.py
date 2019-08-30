#전화번호부
phoneList = {"남정윤": "010-3061-1970", "정유경": "010-4794-7121", "함지현": "010-9089-2341"}

name = input("이름을 입력하세요 : ")
for i in phoneList:
    if name in i:
        print(i+" : "+phoneList[i])


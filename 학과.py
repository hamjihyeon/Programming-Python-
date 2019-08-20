#학번 => 학년 학과 반 번호 (if, list)
0
schoolNum = input("학번 입력 : ")
grade = int(schoolNum[0])
cl = int(schoolNum[1])
num = int(schoolNum[2:])3
majors = [   
            ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
            ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
            ["인터랙티브미디어과", "뉴미디어디자인과", "뉴미디어솔루션과"]
        ]

major = majors[grade-1][(cl-1)//2]

print(str(grade) + "학년 " + str(major) + " " + str(cl) + "반 " + str(num) + "번")
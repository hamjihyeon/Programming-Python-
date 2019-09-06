#국어, 영어, 수학, 자바, 파이썬, JSP 점수 입력받기
#총점, 평균 구하기
#용돈 구하기
#   90점 이상 100000원
#   80점 이상 80000원
#   70점 이상 70000원
#   60점 이상 60000원
#   그 미만은 50000원

k = input("국어 점수를 입력하세요 : ")
e = input("영어 점수를 입력하세요 : ")
m = input("수학 점수를 입력하세요 : ")
j = input("자바 점수를 입력하세요 : ")
p = input("파이썬 점수를 입력하세요 : ")
js = input("JSP 점수를 입력하세요 : ")

sum = int(k) + int(e) + int(m) + int(j) + int(p) + int(js)
print("총점 : ",sum)
avg = sum/6
print("평균 : ", round(avg,2))

if avg >= 90:
    print("용돈 : 100000원")
elif avg >=80:
    print("용돈 : 80000원")
elif avg >=70:
    print("용돈 : 70000원")
elif avg >= 60:
    print("용돈 : 60000원")
else:
    print("용돈 : 50000원")
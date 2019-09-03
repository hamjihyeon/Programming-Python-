from datetime import datetime

print("현제 날짜 시각 객체 얻기")
today = datetime.now()
print("today = datetime.now() : ", today)
print("년 월 일 : ", today.year, today.month, today.day)
print("시 분 초: ", today.hour, today.minute, today.second)
print("요일 : ", today.weekday())
print("특정 날짜 시각 객체 만들기")
day = datetime(2019, 1, 1, 0, 0, 0)
print("day = datetime(2019, 1, 1, 0, 0, 0) : ", day)
print("2019년부터 지나온 시간 구하기")
print("today - day : ", today - day)
print()

#태어난 지 몇 일 지났는지
print("태어난 지 몇일 지났는지")
birth = datetime(2002, 3, 18, 3, 8, 7)
print(today - birth)
print()
#올해 크리스마스 몇일 남았는지
print("올해 크리스마스 몇일 남았는지")
birth = datetime(2019, 12, 24, 0, 0, 0)
print(birth-today)
print()
#내년 내 생일 몇일 남았는지
print("내년 내 생일 몇일 남았는지")
birth = datetime(2020, 3, 18, 0, 0, 0)
print(birth-today)
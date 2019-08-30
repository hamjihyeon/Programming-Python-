# 2419 함지현
# 매점에서 음식을 주문할 때 사용한다.
# 내가 계산할 돈을 주고 거스름돈도 받을 수 있다.
class Eat:
    def __init__(self):
       self.menu = ['','썬칩', '오잉', '콘칩', '빠삐코', '구구콘', '보석바', '포카리', '드링크', '토레타']
       self.price = [0,1500, 1500, 1500, 1000, 1500, 700, 1000, 500, 1500]
       self.bill = [0, 500, 1000, 1500, 5000, 10000, 20000, 50000]
       self.total = 0

    # 메뉴 보여주기
    def show_menu(self):
        i = 1
        print("=========================================")
        print()
        while i< len(self.menu):
            print(i, self.menu[i], self.price[i],"원")
            print()
            i = i+1
        print("=========================================")

    # 음식선택하기
    def choose_menu(self):
        p = int(input("음식을 선택하세요: "))
        n = int(input("개수를 선택해주세요: "))
        price_sum = self.price[p]*n
        print()
        print(self.menu[p], self.price[p],"원 ")
        print(self.menu[p],"총금액: ", self.price[p]*n,"원 입니다.")

        # 음식추가하기
        while p != 0:
            print()
            p = int(input("추가 주문은 음식 번호, 계산은 0을 누르세요: "))
            if p > 0 and p < len(self.menu):
                n = int(input("개수를 선택해주세요: "))
                price_sum = price_sum + self.price[p]*n
                print()
                print(self.menu[p],("이/가 추가되었습니다."))
                print(self.menu[p], self.price[p]," 원 ")
                print(self.menu[p], "총금액: ",self.price[p]*n," 원 ")
            else :
                if p == 0 :
                    print("주문이 완료되었습니다.")
                    print()
                    print( "총금액: ", price_sum, " 원")
                    print()
                    break
                else :
                    print("다시입력해주세요.")
        self.total += price_sum
        return price_sum

    # 지불하기
    def menu_pay(self, total_price):
        # 지불 방법 출력하기
        for i in range (1, len(self.bill)):
            print( i,self.bill[i],"원",end="   ")
        print()

        # 지불액 정하기
        # 총지불액 보여주기
        # 거스름돈 보여주기
        pay = 0
        while pay < total_price:
            p = int(input("지불 금액을 입력하세요 : "))
            print()
            if p>0 and p<len(self.bill):
                pay = pay + self.bill[p]
                if pay-total_price<0:
                    print("돈이 더 필요해요")
                    print("필요한 금액: ", total_price-pay)
                print()
            else :
                print('다시 선택하세요.')

        print("총 지불액: ", pay," 원")
        print("거스름돈: ", pay-total_price, " 원")
        print()
        print("나중에 또 이용해주세요.")

#보여주기
Eat().show_menu()
total_price = Eat().choose_menu()
Eat().menu_pay(total_price)
from coffee import Coffee
from bubbletea import Bubbletea

class Order:
    _menus =[Coffee("아메리카노", 1800), Bubbletea("딸기요거트", 3500)]
    
    def __init__(self):
        self.order_menu =[]
        self.order = None
    
    def show_menu(self):
         print("0: 아메리카노 1800원, 1: 딸기요거트 3500원")

    def sum_price(self):
        sum = 0
        for drink in self.order_menu:
            sum +=drink.price

        return sum

    def order_drink(self):
        # 반복♥
        while True:
            # 메뉴 보여주자
            self.show_menu()
            # 주문받자
            # 음료선택하자
            self.order= input("음료를 선택하세요: ")
            #   음료객체생성하자
            if self.order == "":   #메뉴 선택 안하고 그냥 엔터치면 주문 끝
                break
            if int(self.order) == 0:
                drink = Coffee("아메리카노", 1800)
            elif int(self.order) ==1:
                drink = Bubbletea("딸기요거트", 3500)
            # drink = Order._menus[int(self.order)]
            #   음료옵션정하자
            drink.order()
            #   주문한 음료 리스트에 추가하자
            self.order_menu.append(drink)
            # 반복▲
            # 주문한 음료 추가하자
            for drink in self.order_menu:
                print(drink)
            # 금액 합계구하자
            print("총급액: "+str(self.sum_price())+"원")


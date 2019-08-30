#아마스빈 주문 앱
#Drink <- Coffee
#      <- Bubbletea
#Order
#   메뉴 보여주자
#   음료 보여주자
#   주문한 음료 보여주지
#   총 금액 계산하자

class Drink:
    _cups = ["레귤러", "점보"]
    _ices = ["0%", "50%","100%", "150%"]
    _sugars = ["0%", "50%", "100%", "150%"]

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0
        self.ice = 2
        self.sugar = 2

    def __str__(self):
        return "이름: "+self.name+ "\t가격: "+str(self.price)+"원\t컵: "+Drink._cups[self.cup]+"\t얼음량: "+Drink._ices[self.ice]+"\t당도: "+Drink._sugars[self.sugar]

    def set_cup(self):
        self.cup = input("컵을 선택하세요(0: 레귤러, 1: 점보)")
        if self.cup == "":
            self.cup = 0
        else:
            self.cup = int(self.cup)

        #점보면 300원 추가
        if self.cup == 1:
            self.price += 300

    def set_ice(self):
        self.ice = input("얼음량을 선택하세요.(0: 0%, 1: 50%, 2: 100%, 3: 150%)")
        if self.ice == "":
            self.ice = 2
        else:
            self.ice = int(self.ice)

    def set_sugar(self):
        self.sugar = input("당도를 선택하세요.(0: 0%, 1: 50%, 2: 100%, 3: 150%)")
        if self.sugar == "":
            self.sugar = 2
        else:
            self.sugar = int(self.sugar) 

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

class Coffee(Drink):    #Drink 상속
    pass

class Bubbletea(Drink):
    _pearls = ["타피오카", "코코", "젤리", "알로에"]
    
    def __init_(self, name, price):
        super().__init__(name, price)
        self.pearl = 0

    def set_pearl(self):
        self.pearl = input("펄을 선택하세요(0: 타피오카, 1: 코코, 2: 젤리, 3:알로에)")
        if self.pearl == "":
            self.pearl = 0
        else:
            self.pearl = int(self.pearl)

    def __str__(self):
        return super().__str__() + "\t펄: " + Bubbletea._pearls[self.pearl]

    def order(self):
        super().order()
        self.set_pearl()

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
            drink = Order._menus[int(self.order)]
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

o = Order()
o.order_drink()

# 아메리카노 = Coffee("아메리카노", 1800)
# 아메리카노.order()
# print(아메리카노)   #이름: 아메리카노 \t가격: 1800
# 딸기요거트 = Bubbletea("딸기요거트", 3500)
# 딸기요거트.order()  
# print(딸기요거트)

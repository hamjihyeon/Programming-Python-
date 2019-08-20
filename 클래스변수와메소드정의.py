class Car:
    count = 0


    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, type, speed):
            self.type = type
            self.speed = speed
            Car.count += 1

print(Car.get_count())
c1 = Car("스포츠카", 100)
c2 = Car("트럭", 50)
c3 = Car("벤츠", 300)
print(Car.get_count())
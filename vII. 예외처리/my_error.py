#219p
# class MyError(Exception):
#     pass

class OddError(Exception):  #홀수
    def __init_(self,message = "홀수는 ㄴㄴ"):
        self.message = message

        def __init_(self):
            return self.message

n = 11
try:
    if n % 2 != 0:  #홀수
        raise OddError
    else:   #짝수
        print(n,", n/2 = ", n/2)
except OddError as o:
    print("에러 발생", o)

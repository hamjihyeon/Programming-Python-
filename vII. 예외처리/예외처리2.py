f = open("file.txt", "w")
try:
    f.write("Hello World!")
    f.write(100)
    # f.write(100)    #TypeError: write() argument must be str, not int
except NameError:
    print("이름 에러")
except TypeError:
    print("100은 쓸 수 없음")
except:
    print("모르는 에러")
finally:
    f.close()
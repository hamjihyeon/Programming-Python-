f = open("file.txt", "a")   #a = 덮어쓴다, 다시 실행해도 계속 써진다.
f.write("Hello")
f.write("\n")
f.write("World")

f.close()
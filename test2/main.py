inter1, inter2, opera = input().split()
inter1 = int(inter1)
inter2 = int(inter2)

result = eval("inter1 %s inter2" % opera)
if not result % 1:
    print(int(result))
else:
    print("%.2f" % result)

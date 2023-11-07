def check(n):
    for i in n:
        if i != 0 :
            return False
    return True
n = []
b = 28151
tong = int((b+1) * b / 2)
tong -= b
tong1 = tong
check = 0
for i in range(2,b):
    for j in range(1000000):
        tong1 -= pow(i,j,b)
        if (tong1 == 0) :
            print(i,"Yes")
            tong1 = tong
            check = 1
            break
        elif (tong1 < 0) :
            tong1 = tong
            print(i,"No")
            break
    if (check == 1) :
        break
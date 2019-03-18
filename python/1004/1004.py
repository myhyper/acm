import math
debug = True
debug = None

if debug:
    f = open("input1004.txt")
    ip = f.readline()
else:
    ip = input()
t = int(ip)
#if debug: print(t)


def col(x1, y1, cx1, cy1, r):
    x = x1 - cx1
    y = y1 - cy1

    if abs(x) <= r and abs(y) <= r:
        d = math.sqrt(x**2 + y**2)
        if d <= r:
            return 1
    return 0


for i in range(t):
    #print(i)
    if debug:
        ip = f.readline()
    else:
        ip = input()
    x1,y1,x2,y2 = list(map(int, ip.split(" ")))
    
    if debug:
        ip = f.readline()
    else:
        ip = input()
    n = int(ip)

    cnt = 0
    for j in range(n):
        if debug:
            ip = f.readline()
        else:
            ip = input()
        #print(ip)
        cx1,cy1,cr1 = list(map(int, ip.split(" ")))
        v1 = col(x1,y1,cx1,cy1,cr1)
        v2 = col(x2,y2,cx1,cy1,cr1)

        if v1 != v2:
            cnt += 1
    print("{}".format(cnt))
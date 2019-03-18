import math
debug = True
debug = None

if debug:
    f = open("input1002.txt")
    t = int(f.readline())
else:
    t = int(input())


for a in range(t):
    if debug:
        arr = list(map(int, f.readline().split(" ")))
    else:
        arr = list(map(int, input().split(" ")))
    x1,y1,r1,x2,y2,r2 = arr
    dif = abs(r1 - r2)

    w = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    #print ("w={} diff={} r1={}r2={} r1r2={} c={}".format(w,dif, r1,r2,r1+r2,dif + max(r1,r2)))
    if x1==x2 and y1==y2 and r1 == r2:
        print(-1)
    elif x1==x2 and y1==y2 and r1 != r2:
        print(0)
    elif w < r1 + r2 and dif < w:
        print(2)
    elif w == r1+r2 or w == dif:
        print(1)
    else:
        print(0)


if debug:
    f.close
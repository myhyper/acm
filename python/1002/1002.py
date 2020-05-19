import math
import sys
f = sys.stdin.readline
debug = True
#debug = False
if debug: f = open('input1002.txt').readline
t = int(f())
for _ in range(t):
    arr = list(map(int, f().split()))
    x1,y1,r1,x2,y2,r2 = arr
    dif = abs(r1 - r2)
    w = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if   x1==x2 and y1==y2 and r1 == r2:    ans = -1
    elif x1==x2 and y1==y2 and r1 != r2:    ans =  0
    elif w <  r1 + r2 and dif <  w:         ans =  2
    elif w == r1 + r2 or  w   == dif:       ans =  1
    else:                                   ans =  0
    print(ans)
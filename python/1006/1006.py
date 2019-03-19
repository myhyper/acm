import sys
f = sys.stdin
debug = True
#debug = None
if debug: f = open("1006b.txt")
tc = int( f.readline() )

def calc( idx, prev, last ):
    result = dp[idx][prev][last]
    if result != -1: return result
    inner, outer, both = False, False, False
    
    tmp = (idx + N) % N
    inner = w[0][idx] + w[0][tmp] <= n
    outer = w[1][idx] + w[1][tmp] <= n
    both = w[0][idx] + w[1][idx] <= n
    
    if idx == N - 1:
        if idx == 0: 
            if both: return 1
            else: return 2
        result = 2 
        if last == 0: 
            if inner and not (prev & 1):  result = 1 
            if outer and prev < 2: result = 1 
            if both: result = 1 
            if inner and outer and prev == 0: result = 0 
        elif last == 1: 
            if outer and prev < 2: result = 1
        elif last == 2: 
            if inner and not (prev & 1): result = 1
        return result
    
    tmp = 0
    if idx: tmp = last
    result = 2 + calc(idx + 1, 0, tmp)
    
    if inner and not (prev & 1):
        tmp = 1
        if idx: tmp = last 
        result = min(result, 1 + calc(idx + 1, 1, tmp))
    if outer and prev < 2:
        tmp = 2
        if idx: tmp = last
        result = min(result, 1 + calc(idx + 1, 2, tmp))
    if inner and outer and prev == 0:
        tmp = 3
        if idx: tmp = last
        result = min(result, calc(idx + 1, 3, tmp))
    if both:
        tmp = 0
        if idx: tmp = last 
        result = min(result, 1 + calc(idx + 1, 3, tmp))
    return result

for t in range(tc):
    ip = f.readline()
    if '\n' ==ip: ip = f.readline()
    N,n = map(int, ip.split())
    w=[]
    w.append(list(map(int, f.readline().split())))
    w.append(list(map(int, f.readline().split())))
    dp  = [ [ [-1]*4 for i in range(4) ]*4 for i in range(10000) ]

    print( calc(0,0,0) )

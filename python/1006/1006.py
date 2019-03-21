import sys
f = sys.stdin
debug = True
#debug = None
if debug: f = open("1006.txt")
tc = int( f.readline() )
ii = 0
def calc( idx, prev, last ):
    global ii
    result     = dp[idx][prev][last]
    if result != -1: return result
    inner, outer, both = False, False, False
    
    tmp   = (idx + N) % N
    inner = w[0][idx] + w[0][tmp] <= n
    outer = w[1][idx] + w[1][tmp] <= n
    both  = w[0][idx] + w[1][idx] <= n
    
    if debug: print("({}) {} {} {}".format(ii, idx,prev,last))
    ii += 1
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
    param = 0
    added = 2
    result = added + calc(idx + 1, param, tmp)
    
    if inner and not (prev & 1):
        tmp = 1
        if idx: tmp = last 
        param = 1
        added = 1
        result = min(result, added + calc(idx + 1, param, tmp))
    if outer and prev < 2:
        tmp = 2
        if idx: tmp = last
        param = 2
        added = 1
        result = min(result, added + calc(idx + 1, param, tmp))
    if inner and outer and prev == 0:
        tmp = 3
        if idx: tmp = last
        param = 3
        added = 0
        result = min(result, added + calc(idx + 1, param, tmp))
    if both:
        tmp = 0
        if idx: tmp = last 
        param = 3
        added = 1
        result = min(result, added + calc(idx + 1, param, tmp))
    return result

for t in range(tc):
    ip = f.readline()
    if '\n' ==ip or '' ==ip: ip = f.readline()
    N,n = map(int, ip.split())
    w=[]
    w.append(list(map(int, f.readline().split())))
    w.append(list(map(int, f.readline().split())))
    dp  = [ [ [-1]*4 for i in range(4) ]*4 for i in range(10000) ]
    print( calc(0,0,0) )
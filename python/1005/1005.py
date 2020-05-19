import sys
debug = True
#debug = None
if debug: import time
if debug: start_time = time.time()
f = sys.stdin
if debug: f = open("1005.txt")

tc = int( f.readline() )
for t in range(tc):
    n,k = map(int, f.readline().split())
    w = [0]
    w+= list(map(int, f.readline().split()))
    arr = [ [] for i in range(n+1) ]
    dp    = [0] * (n+1)
    stack = []
    for i in range(k):
        a,b = list(map(int, f.readline().split()))
        arr[b].append(a)
    dst = int( f.readline() )
    dx = dst
    while True:
        if 0 < len(arr[dx]):
            sx = arr[dx][-1]
            if 0 < len(arr[sx]):
                stack.append(dx)
                dx = sx
            else:
                #if debug: print("{} => {}".format(sx,dx))
                val = max(dp[sx],w[sx]) + w[dx]
                if dp[dx] < val: dp[dx] = val 
                if 0 < len(arr[dx]): arr[dx].pop()
                else: dx = stack.pop()
        else: # return phase
            if dx == dst: break
            dx = stack.pop()
    print(dp[dst])
if debug: elapsed_time = time.time() - start_time
if debug: print("time={}".format(elapsed_time))
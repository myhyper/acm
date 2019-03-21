import sys
f = sys.stdin
debug = True
#debug = None
if debug: f = open("1006.txt")
tc = int( f.readline() )
def calc( idx, prev, last ):
    result     = dp[idx][prev][last]
    if result != -1: return result
    ii = 0

    idx1 = idx
    prev1 = prev
    last1 = last
    for i in range(N):
        for j in range(4):
            for k in range(4):
                a = 0
                if 0 < j: a = 1
                b = 0
                if 0 < k: b = 1
                idx2 = idx1 + a + b
                prev2 = prev1
                last2 = last1
                if debug: print("({}) {} {} {}".format(ii, idx2,prev2,last2))
                result1     = dp[idx1][prev1][last1]
                if result1 != -1:
                    result = result1
                    dp[idx1][prev1][last1] = -1
                    break
                inner, outer, both = False, False, False
                result1     = dp[idx2][prev2][last2]
                
                tmp   = (idx2 + N) % N
                inner = w[0][idx2] + w[0][tmp] <= n
                outer = w[1][idx2] + w[1][tmp] <= n
                both  = w[0][idx2] + w[1][idx] <= n

                ii += 1

for t in range(tc):
    ip = f.readline()
    if '\n' ==ip or '' ==ip: ip = f.readline()
    N,n = map(int, ip.split())
    w=[]
    w.append(list(map(int, f.readline().split())))
    w.append(list(map(int, f.readline().split())))
    dp  = [ [ [-1]*4 for i in range(4) ]*4 for i in range(10000) ]
    print( calc(0,0,0) )
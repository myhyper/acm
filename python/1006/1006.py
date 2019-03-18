import sys
f = sys.stdin
debug = True
#debug = None
if debug: f = open("1006a.txt")
tc = int( f.readline() )
for t in range(tc):
    l,n = map(int, f.readline().split())
    w=[]
    w.append(list(map(int, f.readline().split())))
    w.append(list(map(int, f.readline().split())))
    dp = [ [0]*l for i in range(2) ]

    idx = 1
    for i in range(l+1):
        y = 0
        x = i%l

        #if debug: print("({},{}) =>".format(x,y))
        dx = x + 1
        if l <= dx: dx -= l
        ddx = x + 2
        if l <= ddx: ddx -= l

        ## Pr1
        if dp[0][x] == 0 and 0 == dp[1][x] and \
            w[0][x] + w[1][x] <= n and w[0][dx] + w[1][dx] <= n:
            dp[0][x] = idx
            dp[1][x] = idx
            #if debug: print("\t case 1 ({})".format(idx))
            idx += 1 
        elif dp[0][x] ==0 and dp[0][dx] == 0 and 0 == dp[1][x] and 0 == dp[1][dx] and \
            w[0][x] + w[0][dx] <= n and w[1][x] + w[1][dx] <= n:
            dp[0][x] = idx
            dp[0][dx] = idx
            #if debug: print("\t case 2 ({})".format(idx))
            idx += 1 
            dp[1][x] = idx
            dp[1][dx] = idx
            #if debug: print("\t case 2 ({})".format(idx))
            idx += 1 
        ## Pr2
        elif dp[0][x] == 0 and 0 == dp[1][x] and \
            w[0][x] + w[1][x] <= n:
            dp[0][x] = idx
            dp[1][x] = idx
            #if debug: print("\t case 3 ({})".format(idx))
            idx += 1 
        else:
            if i<1: continue
            if dp[0][x] ==0 and dp[0][dx] == 0 and \
                w[0][x] + w[0][dx] <= n:
                dp[0][x] = idx
                dp[0][dx] = idx
                #if debug: print("\t case 4 ({})".format(idx))
                idx += 1 
                if 0 == dp[1][x]:
                    dp[1][x] = idx
                    #if debug: print("\t case 4-2 ({})".format(idx))
                    idx += 1 
            elif dp[1][x] == 0 and dp[1][dx] == 0 and \
                w[1][x] + w[1][dx] <= n:
                dp[1][x] = idx
                dp[1][dx] = idx
                #if debug: print("\t case 5 ({})".format(idx))
                idx += 1 
                if 0 == dp[0][x]:
                    dp[0][x] = idx
                    #if debug: print("\t case 5-2 ({})".format(idx))
                    idx += 1 
            ## Pr3
            else:
                if 0 == dp[0][x]:
                    dp[0][x] = idx
                    #if debug: print("\t case 6 ({})".format(idx))
                    idx += 1
                if 0 == dp[1][x]:
                    dp[1][x] = idx
                    #if debug: print("\t case 7 ({})".format(idx))
                    idx += 1
                #if debug: print("\t case 8 ({})".format(idx))

    if debug: print(w[0])
    if debug: print(w[1])
    if debug: print(dp[0])
    if debug: print(dp[1])
    print(idx-1)
import sys
f = sys.stdin
debug = True
#debug = None
if debug: f = open("1006.txt")
tc = int( f.readline() )

wes = [3,3,3, 4,4,4,4,4,4,4,4,4, 5,5,5,5,5,5,5, 6]
pri = [
    # 1
    [0,1,2,
     0,1,2],
    # 2
    [0,1,1,
     0,2,2],
    # 3
    [0,0,2,
     1,1,2],
    # 4
    [0,1,2,
     3,1,2],
    # 5
    [0,1,2,
     0,1,3],
    # 6
    [0,1,1,
     0,2,3],
    # 7
    [0,1,2,
     0,3,3],
    # 8
    [0,0,3,
     1,2,3],
    # 9
    [0,1,2,
     3,3,2],
    # 10
    [0,1,2,
     0,3,2],
    # 11
    [0,1,1,
     2,2,3],
    # 12
    [0,0,1,
     2,3,3],
    # 13
    [0,1,2,
     3,1,4],
    # 14
    [0,1,1,
     2,3,4],
    # 15
    [0,1,2,
     3,4,4],
    # 16
    [0,0,1,
     2,3,4],
    # 17
    [0,1,2,
     3,3,4],
    # 18
    [0,1,2,
     3,4,2],
    # 19
    [0,1,2,
     0,3,4],
    # 20
    [0,1,2,
     3,4,5],
]
for t in range(tc):
    l,n = map(int, f.readline().split())
    w=[]
    w.append(list(map(int, f.readline().split())))
    w.append(list(map(int, f.readline().split())))
    dp  = [ [0]*l for i in range(2) ]
    pts = [ [0]*l for i in range(2) ]

    idx = 1
    for i in range(l):
        x = i%l

        if debug: print("({}) =>".format(x))

        for p in range(len(pri)):
        #for p in range(1):
            matched = True
            ss = [0] * 6
            xx = -1
            for dy in range(2):
                for ddx in range(-1,2):
                    xx += 1
                    dx = ddx + x
                    if l <= dx: dx -= l
                    if dx < 0:  dx += l
                    #if debug: print("\t{},{}".format(dx,dy))

                    if 0 != dp[0][x] and 0 != dp[1][x]:
                        matched = False
                        #if debug: print("skipped")
                        break ## already filled
                    if 0 != dp[0][x] or 0 != dp[1][x]:
                        if pri[p][1] == pri[p][4]:
                            matched = False
                            #if debug: print("pattern {} skipped".format(p+1))
                            break ## already filled
                
                    ii = pri[p][xx]
                    ss[ii] += w[dy][dx]
                    #print("pz = {}".format(ii))
                    #print(ss)
                    if n < ss[ii]:
                        matched = False
                        break
                    # consider the previous block
                    if 0 != dp[0][dx] and -1 == ddx:
                        if pri[p][0] != pri[p][3]:
                            if dp[0][dx] == dp[1][dx]:
                                matched = False
                                break
                        else:
                            if dp[0][dx] != dp[1][dx]:
                                matched = False
                                break
                    # consider the next block
                    if 0 != dp[0][dx] and 1 == ddx:
                        if pri[p][2] != pri[p][5]:
                            if dp[0][dx] == dp[1][dx]:
                                matched = False
                                break
                        else:
                            if dp[0][dx] != dp[1][dx]:
                                matched = False
                                break
                    # blocked prev and next exception
                    if 0 != dp[0][dx] and -1 == ddx:
                        sx = ddx + 1
                        if l <= sx: sx -= l
                        if 0 != dp[0][sx]:
                            if w[0][x] + w[1][x] <= n:
                                if pri[p][1] != pri[p][4]:
                                    matched = False
                                    break
                            
                if matched == False: break
            if matched == True:
                if debug: print("pattern {} matched cnt={} ".format(p+1, wes[p]))
                found = False
                xx = -1
                for dy in range(2):
                    for dx in range(-1,2):
                        xx += 1
                        dx += x
                        if l <= dx: dx -= l
                        if dx < 0:  dx += l
                        if 0 == dp[dy][dx] and pri[p][xx] == pri[p][1]:
                            #print("\tx {},{} xx={} pri[p][1]={}".format(dx,dy,xx,pri[p][1]))
                            dp[dy][dx] = idx
                            pts[dy][dx] = p
                            found = True    
                if found: idx += 1
                print(dp[0])
                print(dp[1])

                found = False
                xx = -1
                for dy in range(2):
                    for dx in range(-1,2):
                        xx += 1
                        dx += x
                        if l <= dx: dx -= l
                        if dx < 0:  dx += l
                        if 0 == dp[dy][dx] and pri[p][xx] == pri[p][4]:
                            #print("\tx2 {},{}".format(dx,dy))
                            dp[dy][dx] = idx
                            pts[dy][dx] = p
                            found = True    
                if found: idx += 1
                print(dp[0])
                print(dp[1])
                print("")
                break
            else:
                #print("parttern {} not matched, next".format(p+1))
                a=1
        # else case
        if dp[0][x] == 0:
            dp[0][x] = idx
            pts[0][x] = -p
            idx += 1
        if dp[1][x] == 0:
            dp[1][x] = idx
            pts[1][x] = -p
            idx += 1


    if debug: print(w[0])
    if debug: print(w[1])
    if debug: print(pts[0])
    if debug: print(pts[1])
    print(idx-1)
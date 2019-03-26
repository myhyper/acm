import sys
f = sys.stdin
debug = True
#debug = None
if debug: f = open("1006b.txt")
tc = int( f.readline() )
if debug: import time
if debug: start_time = time.process_time()

pattern1 = [
    [ [1,4], ],
    [ [0,1],[4] ],
    [ [1],[3,4], ],
    [ [0,1],[3,4], ],
    [ [0,1],[4,5], ],
    [ [1],[4] ],
    [ [1,2],[4], ],
    [ [1],[4,5], ],
    [ [1,2],[4,5], ],
    [ [1,2],[3,4], ],
]

def check_pattern(i):
    rtv = []
    for j in range(len(pattern1)):
        tmp = True
        for arr in pattern1[j]:
            s = 0
            for k in arr:
                y = int(k / 3)
                x = int((k % 3 - 1 + i + l) % l)
                s += w[y][x]
            if n < s: # 지정된 두 칸의 합이 n을 넘어가면 이 패턴 적용 불가.
                tmp = False
                break
        if tmp: rtv.append(j)
    return rtv # 가능한 노드를 배열로 리턴 한다.

# s->d 패턴 으로 이동 가능한지 검사 한다.
# 이동 불가시 -1를 리턴 하고 가능할때는 비용 0,1,2 중 하나를 리턴 한다.
def check_move(s,d): 
    cost_group_1 = [0,1,2,4,9]
    if s == 8 and d == 3: cost = 0
    elif d in cost_group_1: cost = 1
    else: cost = 2

    source_group = [0,1,2,3,5]
    destination_group = [0,5,6,7,8]

    if s in source_group and d in destination_group: return cost
    if (s == 4 or s == 7) and (d == 2 or d == 9): return cost
    if (s == 6 or s == 9) and (d == 1 or d == 4): return cost
    if s == 8 and d == 3: return cost
    return -1

for t in range(tc):
    ip = f.readline()
    if '\n' ==ip: ip = f.readline()
    l,n = map(int, ip.split())
    w=[]
    w.append(list(map(int, f.readline().split())))
    w.append(list(map(int, f.readline().split())))

    ans = 0
    skip = 0
    last = -1
    for i in range(l):
        print("i={}".format(i))
        if 0 < skip:
            skip -= 1
            continue
        p1 = check_pattern((i-1+l)%l)
        p2 = check_pattern((i+0+l)%l)

        if l == 1:
            min_val = 999999
            for j in p1:
                a = check_move(j,j)
                if -1 == a: continue
                val = a
                if val < min_val:
                    min_val = val
            ans = min_val
        elif l == 2:
            min_val = 999999
            for k in p2:
                for j in p1:
                    a = check_move(k,j)
                    b = check_move(j,k)
                    if -1 == a or -1 == b: continue
                    val = a + b
                    if val < min_val:
                        min_val = val
            ans = min_val
        else:
            break
            #print(p1)
            min_val = 9999998
        ans = min_val
        print("")
        #break # for i


    #print(p1)
    if 0 == ans:
        dp = [ [9999998] * 10 for _ in range(l) ]
        for i in range(l):
            for j in range(10):
                dp[i][j] = 1

        for dp in dp:
            print(dp)
    print("")

    #print(w[0])
    #print(w[1])
    #print(dp)
    print(ans)
    break #tc

if debug:
    print("= {0:0.4f} seconds".format(time.process_time() - start_time))
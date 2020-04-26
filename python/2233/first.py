import sys
f = sys.stdin.readline
dbg = 1
if dbg:  f = open("input.txt").readline
T = int(f())

arr = f()
a,b = map(int,(f().split()))
print(a,b)
lv = 1
idx = 1

alpha = "aabcdefghijklmnopqrstuvwxyz"
nodes = []
is_first = False

max_len = 10
tree = [ [] for _ in range( max_len ) ]
tmp = 0

lv_a = -1
lv_b = -1

for ch in arr.strip():
    if '0' == ch:
        if len(nodes):
            last = nodes[-1]
        else:
            last = 0
        # tree[tmp].append(last)
        nodes.append(last + 1)
        print(idx, " : 0 lv : ", (lv-0), " => ", alpha[ nodes[-1] ], end ='')
        lv += 1
        is_first = True
        tmp = nodes[-1]
    else:
        if is_first:
            is_first = False
            print(idx, " : 1 lv : ", (lv-2), " => ", alpha[ nodes[-1] ], end ='')
            tmp = nodes[-1]
        else:
            print(idx, " : 1 lv : ", (lv-2), " => ", alpha[ lv-1 ], end ='')
            tmp = lv-1
        lv -= 1
    if a == idx or b == idx:
        print(" ← wormy", end = '')
        if -1 == lv_a:
            lv_a = lv -1
            print("lv_a = ", lv_a)
        elif -1 == lv_b:
            lv_b = lv -1 
            print("lv_b = ", lv_b)
        else:
            ans = min(lv_a, lv_b) + 
    print('')
    idx += 1
print( tree )
print( nodes )
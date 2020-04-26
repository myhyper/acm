import sys
f = sys.stdin.readline
dbg = 1
prt = 1
if dbg:  f = open("input1.txt").readline

N = int(f())
arr = f()
L = len(arr)
a,b = map(int,(f().split()))
# alpha = "abcdefghijklmnopqrstuvwxyz"

st = []
cnt = 0
idx = 0
st_a = st_b = None
for ch in arr.strip():
    if prt: print(ch, end='')
    if ch == '0':
        # tmp = alpha[cnt]
        tmp = cnt
        st.append( tmp )
        cnt += 1
    else:
        tmp = st.pop()
    idx += 1
    if a == idx or b == idx:
        if prt: print(st, '\t\t(',tmp, '<= wormy )')
        if None == st_a:
            st_a = st.copy()
        else:
            st_b = st.copy()
    else:
        if prt: print(st, '\t\t(',tmp, ' )')
length = min( len(st_a), len(st_b) )
common = []
for _ in range(length):
    if st_a[_] != st_b[_]:
        break
    else:
        common = st_a[0:_+1]
if prt: print(common)
if prt: print('')

st = []
cnt = 0
idx = 0
ans1 = ans2 = 0
st_a = st_b = None
for ch in arr.strip():
    if prt: print(ch, end='')
    if ch == '0':
        # tmp = alpha[cnt]
        tmp = cnt
        st.append( tmp )
        cnt += 1
        if st == common:
            if prt: print('ok2',st,common,idx+1)
            ans1 = idx+1
    else:
        if st == common:
            if prt: print('ok2',st,common,idx+1)
            ans2 = idx+1
        tmp = st.pop()
    idx += 1
    if prt: print(st, '\t\t(',tmp, ' )')

print(ans1, ans2)
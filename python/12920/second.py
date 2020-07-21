import sys
sys.setrecursionlimit(999999)
f = sys.stdin.readline
dbg = 1;prt = 0
if dbg: f = open('j.txt').readline
N,K = map(int,f().split())
V = [0]; W = [0]
tt = []
for n in range(N):
  w,v,k = map(int, f().split())
  if w <= K:
    tt.append([w,v,k])
for i in range(len(tt)):
  for j in range(len(tt)):
    if i != j:
      if tt[i][0] == tt[j][0]:
        if tt[i][1] == tt[j][1] and 0 < tt[j][2]:
          tt[i][2] += tt[j][2]
          tt[j][2] = 0
for w,v,k in tt:
  # w,v,k = map(int, f().split())
  #if w <= K:
  if 0 < k:
    vo =v; wo =w
    n = 1
    while n <= 5000:
      if n <= k:
        k -= n
        V.append(v*n);W.append(w*n)
        if prt: print(n, k)
      n *= 2
    while 0 < n:
      if n <= k:
        k -= n
        V.append(v*n);W.append(w*n)
        if prt: print(n, k)
      n = int(n/2)
    for kk in range(k):
      V.append(v);W.append(w)
N = len(V)-1
arr = [[''] * (K+1) for _ in range(N+1)]
if prt: print(W)
if prt: print(V)
def visit(i, j):
  if arr[i][j] != '': return arr[i][j]
  if i == 0 or j == 0: rtv = 0
  elif j < W[i]: rtv = visit(i-1, j)
  else:
    a = visit(i-1, j)
    b = V[i] + visit(i-1, j-W[i])
    rtv = max(a, b)
  arr[i][j] = rtv
  return rtv
print(visit(N, K))
#if dbg:
#  for a in arr: print(a)
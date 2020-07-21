import sys
f = sys.stdin.readline
dbg = 1;prt = 0
if dbg: f = open('j.txt').readline
N,K = map(int,f().split())
V = []; W = []
for n in range(N):
  w,v,k = map(int, f().split())
  if w <= K:
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
if prt: print(W)
if prt: print(V)

dp1 = [ 0 for _ in range(K+1) ]
dp2 = [ 0 for _ in range(K+1) ]
def foo():
  for i in range(len(V)):
    if prt: print(i)
    now = dp1;prev = dp2
    if i%2 ==0: prev = dp1;now = dp2
    w = W[i];v = V[i]
    if w <= K: now[w] = max(prev[w],v)
    for j in range(K+1): # <- 배운점: K+1 이어야 했다. K에 딱맞는 비싼 물건 이 있을시. (j.txt 9째줄)
      now[j] = max(now[j], prev[j])
      if 0 < prev[j] and j+w <= K:
        now[j+w] = max(prev[j+w], prev[j]+v)
    # if prt: print(prev);print(now)
foo();print(max(max(dp1),max(dp2)))
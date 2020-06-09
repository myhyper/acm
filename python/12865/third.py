import sys
dbg = 1
prt = 0
f = sys.stdin.readline
if dbg: f = open('0.txt').readline
N,K = map(int,f().split())

W = [ 0 for _ in range(N) ]
V = [ 0 for _ in range(N) ]
for i in range(N):
  W[i], V[i] = map(int,f().split())

M = K + 10
# if dbg: M = 11
dp1 = [ 0 for _ in range(M) ]
dp2 = [ 0 for _ in range(M) ]

if W[0] <= K:
  dp1[0] = 0
  dp1[W[0]] = max(dp1[W[0]], V[0]) # 회전을 고려 해서 max로 init

# dp[무게] = 가치
def foo ():
  for i in range(1, N):
    now = dp2;prev = dp1
    if i % 2 == 0: now = dp1;prev = dp2
    
    w = W[i]; v = V[i]
    if prt: print(i, w, v)
    if w <= K: now[w] = max(prev[w], v)
    for j in range(0, K):
      now[j] = max(prev[j], now[j])
      if j + w <= K and 0 != prev[j]:
        now[j+w] = max(now[j+w], prev[j] + v)
    if prt: print(prev);print(now)
foo();print(max(max(dp1),max(dp2)))
import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('24.txt').readline
N,K = map(int, f().split())
W = [];V = []
for n in range(N):
  w,v = map(int, f().split())
  if w <= K: W.append(w);V.append(v)
  else: N -= 1
dp = [ [ 0 for _ in range(N+1) ] for _ in range(K+1) ]
for i in range(N-1,-1,-1):
  for j in range(K+1):
    dp[j][i] = max(dp[j][i], dp[j][i+1])
    if W[i] <= j:
      dp[j][i] = max(dp[j][i], V[i] + dp[j-W[i]][i+1])
# for d in dp: print(d)
print(max(dp[K]))
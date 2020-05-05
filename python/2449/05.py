# 최적화 한다.
import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('input1.txt').readline
N,K = map(int, f().split())
arr = list(map(int, f().split()))

M = 99999
dp = [[M for _ in range(N)] for _ in range(N)]
for i in range(N): dp[i][i] = 0

def visit(x, y):
  if dp[x][y] != M: return dp[x][y]
  for i in range(x,y):
    j = i + 1
    r = visit(x,i) + visit(j,y)
    if arr[x] != arr[j]: r += 1
    dp[x][y] = min(dp[x][y], r)
  return dp[x][y]

print(visit(0, N-1))
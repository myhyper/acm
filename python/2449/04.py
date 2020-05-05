# 기본 입력을 받는다.
import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('input1.txt').readline
N,K = map(int, f().split())
arr = list(map(int, f().split()))

# test
#print(arr)

# DP를 적용한다.
M = 99999
dp = [[M for _ in range(N)] for _ in range(N)]
for i in range(N): dp[i][i] = 0

# 분할 DP 초석을 다진다.
# 비용을 계산한다.
def visit(x, y):
  if x == y: return 0
  if dp[x][y] != M: return dp[x][y]
  # print(x, '~', y) # test
  dp[x][y] = 9999
  for i in range(x,y):
    j = i + 1
    r = visit(x,i)
    r += visit(j,y)
    if arr[x] != arr[j]: r += 1
    dp[x][y] = min(dp[x][y], r)
  return dp[x][y]

print(visit(0, N-1))
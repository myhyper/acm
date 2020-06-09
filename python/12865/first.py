import sys
sys.setrecursionlimit(99999)
f = sys.stdin.readline
dbg = 1
if dbg: f = open('24.txt').readline
N, K = map(int, f().split())
KG = 0
VAL = 1
arr = [ [0, 0] for _ in range(N) ]
for n in range(N):
  kg, val = map(int, f().split())
  arr[n][KG] = kg
  arr[n][VAL] = val

dp = [ -1 for _ in range(N) ]
def visit(idx):
  total_weight = 0
  max_val = 0
  if idx == N: return 0,0
  if -1 != dp[idx]: return dp[idx]
  for i in range(idx+1, N):
    weight, val = visit(i)
    if weight <= K:
      if max_val < val:
        max_val = val
        total_weight = weight
    
    weight = arr[idx][KG] + weight
    if weight <= K:
      if max_val < val + arr[idx][VAL]:
        max_val = val + arr[idx][VAL]
        total_weight = weight
  dp[idx] = (total_weight, max_val)
  return total_weight, max_val

print(visit(0)[0])
print(visit(0)[1])
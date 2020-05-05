import sys
sys.setrecursionlimit(999999)
f = sys.stdin.readline
dbg = 1 # read input from file or not
prt = 0 # print or not
if dbg: f = open('input1.txt').readline
N,K = map(int, f().split())
arr = list(map(int, f().split()))

M = 99999 # infinite

dp = [ [ M for _ in range(N) ] for _ in range(N) ]
for i in range(N):
  dp[i][i] = 0

def visit(a, x, y, lv):
  if prt:
    for _ in range(lv):
      print('\t',end='')
    print('visi',x,y)
  if dp[x][y] != M:
    if prt:
      for _ in range(lv):
        print('\t',end='')
      print('return1',dp[x][y])
    return dp[x][y]
  rtv = M
  for i in range(x,y):
    j = i+1
    if prt:
      for _ in range(lv):
        print('\t',end='')
      print(x,i, ' + ', j,y)
    c = 1
    if a[x] == a[j]: c = 0
    print(a, a[x:i], a[j:y], a[x], a[j], '=>', c, '(',x,i,j,y,')')
    cost = visit(a, x, i, lv+1) + visit(a, j, y, lv+1) + c
    # dp[s][e] = cost
    if cost < rtv:
      rtv = cost
      if prt:
        for _ in range(lv):
          print('\t',end='')
        print('found =>', cost)
    # rtv = min(rtv, cost)
  if prt:
    for _ in range(lv):
      print('\t',end='')
    print('return', rtv)
    print('')
  dp[x][y] = rtv
  return rtv

ans = visit(arr, 0, N-1, 0)
print(ans)

if prt:
  for d in dp:
    print(d)
import sys
f = sys.stdin.readline
prt = 1
dbg = 1
tdd = 1
if dbg: f = open('8.txt').readline
arr = f()

M = 2010
if dbg:
  M = 12
dp = [[0, 0] for _ in range(M)]
# 그냥 간다
# 합친다
if prt: print(arr)
def visit(a):
  N = len(a)
  dp[0][0] = 1
  for i in range(0, N):
    n = a[i-1] + a[i]
    one = two = False
    if '0' != a[i]: # 안합친다
      one = True
    if 0 < i and '10' <= n and n <= '26': # 합친다
      two = True
    
    if one and two:
      c = max(max(dp[i-1]),max(dp[i-2]))
      dp[i][0] = (c * 2) % 1000000
      dp[i][1] = (c * 2) % 1000000
    else:
      if one:
        dp[i][0] = max(1, max(dp[i-1])) % 1000000
        dp[i][1] = 0
      elif two:
        dp[i][1] = max(1, max(dp[i-2])) % 1000000
        dp[i][0] = 0
      else:
        return 0

  return max(dp[N-1]) % 1000000

#          2 5 1 1 4    1 2 0 1   2 6 2 6 
# 안합친다.  1 1 2 3 5    1 2 0 1   1 1 2 2
# 합친다.   0 2 0 4 6    0 3 1 0   0 2 0 4

print(visit(arr))
if prt: print(dp)


if tdd:
  print("")
  prt=0

  dp = [[0, 0] for _ in range(M)]
  arr = "0"
  ans = visit(arr)
  if ans != 0: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "011"
  ans = visit(arr)
  if ans != 0: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "0101"
  ans = visit(arr)
  if ans != 0: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "1012"
  ans = visit(arr)
  if ans != 2: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "1054"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "7220"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "2626"
  ans = visit(arr)
  if ans != 4: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "2727"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "1070"
  ans = visit(arr)
  if ans != 0: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "1010"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "1020"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "19"
  ans = visit(arr)
  if ans != 2: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "1203"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "28713831"
  ans = visit(arr)
  if ans != 2: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "6398101327"
  ans = visit(arr)
  if ans != 2: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "208227"
  ans = visit(arr)
  if ans != 2: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "1111737"
  ans = visit(arr)
  if ans != 8: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "110"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "100000"
  ans = visit(arr)
  if ans != 0: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "0"
  ans = visit(arr)
  if ans != 0: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "9"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "1111111111"
  ans = visit(arr)
  if ans != 89: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "1203"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [[0, 0] for _ in range(M)]
  arr = "1203"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)
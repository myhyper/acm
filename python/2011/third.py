import sys
f = sys.stdin.readline
prt = 0
dbg = 0
tdd = 0
if dbg: f = open('4_.txt').readline
arr = f()


# 10 1 2
# 10 12

M = 20
dp = [0 for _ in range(M)]

def visit(a):
  dp[0] = 1
  N = len(a)
  cost = 0
  not_merged_at_all = True
  for i in range(N):
    j = i - 1
    n = -1
    if 0 <= j:
      n = (a[j] + a[i])
    if -1 != n and '09' < n and n < '27': # ㅎㅏㅂ쳐지나?
      if '0' != a[i]: # 0이 있나?
        if 1 == i:
          if i < N-1 and '0' == a[i+1]:
            if prt: print("１합쳐지고 0이 없어서 근데 처음이라 근데 그다음이 0 이라합칠수밖에 없어서 그대로", n)
            dp[(i)%M] += dp[(i-1)%M] + 0
          else:
            if prt: print("２합쳐지고 0이 없어서 근데 처음이라 전+1", n)
            dp[(i)%M] += dp[(i-1)%M] + 1
        else:
          if 2 < i and a[i-2] == '0' or not('09' < (a[i-3]+a[i-2]) and (a[i-3]+a[i-2]) < '27'):
            if prt: print("３합쳐지고 0이 없어서 근데 앞번이 0이어서 전+1", n)
            dp[(i)%M] += dp[(i-1)%M] + 1
          else:
            if prt: print("４합쳐지고 0이 없어서 전+2", n)
            if i != N-1:
              cost = 1
            dp[(i)%M] += dp[(i-1)%M] + 2
        not_merged_at_all = False
      else:
        if 1 == i:
          if prt: print("５합쳐지고 0이 있어서 전전+0 근데 i가 작아서 전+0", n)
          dp[(i)%M]  = dp[(i-1)%M]
        else:
          if prt: print("６합쳐지고 0이 있어서 전전+0", n)
          dp[(i)%M]  = dp[(i-2)%M]
    else:
      if '0' != a[i]: # 0이 있나?
        if 0 == i:
          if prt: print("７안합쳐지고 0이 없어서 근데 처음이라 1", a[i])
          dp[i%M] = 1
        else:
          if prt: print("８안합쳐지고 0이 없어서 전+0", a[i])
          dp[(i)%M] = dp[(i-1)%M]
      else:
        if prt: print("９안합쳐지고 0이 있어서 0", a[i])
        return 0
    dp[i%M] %= 1000000
  if not_merged_at_all:
    return dp[(N-1)%M] % 1000000
  if prt: print("not_merged_at_all + 0", 'cost=', cost)
  return (dp[(N-1)%M] + cost) % 1000000

print(visit(arr))
if prt: print(dp)


if tdd:
  print("")
  prt=0

  dp = [0 for _ in range(M)]
  arr = "0"
  ans = visit(arr)
  if ans != 0: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "011"
  ans = visit(arr)
  if ans != 0: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "0101"
  ans = visit(arr)
  if ans != 0: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "1012"
  ans = visit(arr)
  if ans != 2: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "1054"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "7220"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "2626"
  ans = visit(arr)
  if ans != 4: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "2727"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "1070"
  ans = visit(arr)
  if ans != 0: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "1010"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "1020"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "19"
  ans = visit(arr)
  if ans != 2: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "1203"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "28713831"
  ans = visit(arr)
  if ans != 2: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "6398101327"
  ans = visit(arr)
  if ans != 2: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "208227"
  ans = visit(arr)
  if ans != 2: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "1111737"
  ans = visit(arr)
  if ans != 8: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "1203"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "1203"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "1203"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)

  dp = [0 for _ in range(M)]
  arr = "1203"
  ans = visit(arr)
  if ans != 1: print("Err 1", arr, ans)
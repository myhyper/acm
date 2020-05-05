import sys
f = sys.stdin.readline
dbg = 1
prt = 0
if dbg: f = open('input3.txt').readline
N,K = map(int, f().split())
arr = list(map(int, f().split()))
dp = [ [ 0 for _ in range(N) ] for _ in range(N) ]

def press(a):
  l = len(a)
  for i in range(l-2, -1, -1):
    if a[i] == a[i+1]:
      a.pop(i+1)
test = [1,2,3,3,2,2,1,1]
press(test)
if test != [1,2,3,2,1]: print("ERR1", test)

def cut(arr, n):
  cnt = 0
  while n in arr:
    arr.remove(n)
    cnt += 1
  return cnt

# ma = max(arr)
# mi = min(arr)
# ans = 0
# while ma != mi:
#   press(arr)
#   a = arr.count(ma)
#   b = arr.count(mi)
#   print('press', arr)
#   if a == b:
#     ans += cut(arr, ma)
#     ans += cut(arr, mi)
#   elif a < b:
#     ans += cut(arr, ma)
#   else:
#     ans += cut(arr, mi)
#   print('cut', arr, ans)
#   ma = max(arr)
#   mi = min(arr)

dp = {}

for _ in range(21):
  a = [_]
  key = str(a)
  dp[key] = 0

def visit(a, lv):
  if prt and lv <= 2: print(a)
  # key = str(a)
  # if key in dp:
  #   return dp[key]
  cnt = [ 0 for _ in range(21) ]
  k = 0
  for n in a:
    if 0 == cnt[n]:
      k += 1
    cnt[n] += 1
  if 1 == k: return 0
  
  rtv = 9999
  for i in range(21):
    if cnt[i]:
      b = a.copy()
      cost = b.count(i)
      if prt and lv <= 2: print(' remove', i, 'cost is', cost)
      cut(b, i)
      press(b)
      r = visit(b, lv+1) + cost
      if prt and lv <= 2: print(' =>', b)
      if r < rtv:
        rtv = r
        if prt and lv <= 2: print ( ' rtv changed to', r)
  if prt and lv <= 2: print(' return ', rtv)
  if prt and lv <= 2: print('')
  if key in dp:
    dp[key] = min(dp[key], rtv)
  else:
    dp[key] = rtv
  return rtv

press(arr)
ans = visit(arr, 1)

print(ans)
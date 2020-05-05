import sys
sys.setrecursionlimit(99999)
f = sys.stdin.readline
dbg = True
# dbg = False
dbgPrint = True
dbgPrint = False
if dbg: f = open('i.txt').readline
N,K = map(int, f().split())
mArr = list(map(int, f().split()))

dp = {}

def chr(a):
  data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
  rtv = data[a]
  return rtv

def visit(pArr, lv):
  l = len(pArr)
  if 1 == l: return 0
  # key = str(pArr)
  m = min(pArr)
  key = ''.join(chr(i-m) for i in pArr)
  if key in dp:
    return dp[key]
  rtv = 9999
  for i in range(l):
    cost = 1
    if 0 < i and i < l and pArr[i-1] == pArr[i]:
      cost = 0
    if i < l-1 and pArr[i] == pArr[i+1]:
      cost = 0

    arr = pArr.copy()
    arr.pop(i)

    r = visit(arr, lv+1) + cost
    if dbgPrint:
      if lv <= 4:
        print(i, lv, arr, '=>', r)
    if r < rtv: rtv = r
  dp[key] = rtv
  return rtv

ans = visit(mArr, 1)
print(ans)
print(dp)
print(len(dp))
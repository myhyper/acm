import sys
sys.setrecursionlimit(99999)
f = sys.stdin.readline
dbg = True
# dbg = False
dbgPrint = True
# dbgPrint = False
if dbg: f = open('i.txt').readline
N,K = map(int, f().split())
mArr = list(map(int, f().split()))

NONE  = 0
LEFT  = 1
RIGHT = 2
BOTH  = 3

def leftOrRight(arr, i):
  rtv = NONE
  bRight = bLeft = False
  if 0 < i and arr[i-1] == arr[i]:
    bLeft = True
  if i < len(arr)-1 and arr[i] == arr[i+1]:
    bRight = True
  if bLeft and bRight:
    rtv = BOTH
  elif bLeft: rtv  = LEFT
  elif bRight: rtv = RIGHT
  return rtv

dp = {}

def visit(pArr, pAtt, lv):
  l = len(pArr)
  if 1 == l: return 0
  key = str(pArr)
  # if key in dp:
  #   return dp[key]
  rtv = 9999
  for i in range(l):
    cost = 0
    if pAtt[i] == NONE:
      cost = 1

    arr = pArr.copy()
    arr.pop(i)
    att = pAtt.copy()
    att.pop(i)
    if 0 < i:
      att[i-1] = leftOrRight(arr, i-1)
    if i < l-1:
      att[i-0] = leftOrRight(arr, i-0)
    if dbgPrint:
      if lv <= 4:
        print(i, lv, arr, att, '=>', cost)
    r = visit(arr, att, lv+1) + cost
    if r < rtv: rtv = r
  dp[key] = r
  return r
mAttr = [ NONE for _ in range(len(mArr)) ]
for _ in range(len(mArr)):
  mAttr[_] = leftOrRight(mArr, _)
ans = visit(mArr, mAttr, 1)
print(ans)
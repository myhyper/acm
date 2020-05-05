import sys
f = sys.stdin.readline
dbg = 0
if dbg: f = open('input.txt').readline

def press(arr):
  last = -1
  for i in range(len(arr)-1, -1, -1):
    if -1 != last and last == arr[i]:
      arr.pop(i)
    last = arr[i]
  tmp = [ 0 for _ in range(21) ]
  for n in arr:
    tmp[n] += 1
  
  cache = []
  cnt = 0
  for i in range(len(tmp)):
    if 0 < tmp[i]:
      cnt += 1
      cache.append(i)
  
  for i in range(len(arr)):
    arr[i] = cache.index(arr[i]) + 1
  pass
#TDD
u = [1,3,5]
press(u)
if u != [1,2,3]: print("ERR1", u)
u = [1,1,1,1,3,3,3,3,3,3,5,5,5,5,5]
press(u)
if u != [1,2,3]: print("ERR2", u)
u = [1,2,3,3,2,2,1]
press(u)
if u != [1,2,3,2,1]: print("ERR3", u)

N,K = map(int, f().split())
arr = list(map(int, f().split()))
# print(arr)
press(arr)
# print(arr)
dp = {}
def visit(arr):
  key = str(arr)
  if key in dp:
    return dp[key]
  # if dbg: print(arr)
  l = len(arr)
  if 0 == l or 1 == l: return 0

  min_total = 99999
  for i in range(l):
    tmp = list(arr)
    cost = 1
    if (0 < i and arr[i] == arr[i-1]) or (i < l-1 and arr[i] == arr[i+1]):
      cost = 0
    tmp.pop(i)
    total = visit(tmp) + cost
    if total < min_total: min_total = total
  dp[key] = min_total
  return min_total

ans = visit(arr)
print(ans)
import sys
sys.setrecursionlimit(999999)
f = sys.stdin.readline
dbg = 1
o = open('output.txt','w')

# o = sys.stdout
if dbg: f = open('input2.txt').readline
N,K = map(int, f().split())
# print(N)
arr = list(map(int, f().split()))


def paint(idx, color, tmp):
  j = i = idx
  cnt = 0
  if tmp[idx] == color: return 0
  last = tmp[idx]
  while 0 <= i and tmp[i] == last:
    tmp[i] = color
    i -= 1
    cnt += 1
    if idx ==j: j+=1
  while j < N and tmp[j] == last:
    tmp[j] = color
    j += 1
    cnt += 1
  return cnt # was painted or not
best_ans = 99999

# dp
dp = {}
def is_done(tmp):
  return max(tmp) == min(tmp)

# test = [2,1,2,2,2,3]
# N = len(test)
# print(test)
# paint(3,3,test)
# print(test)
# 
# test = [1,2,2,2,3,1]
# print(test)
# paint(2,1,test)
# print(test)

def visit2(cnt, arr1):
  if is_done(arr1):
    return cnt
  key = str(arr1)
  if key in dp:
    return dp[key]
  if K < cnt:
    return K
  rtv = 9999
  for n in range(N-1):
    if n < N-1:
      tmp = list(arr1)
      a = paint(n, arr1[n+1], tmp)
      if a:
        b = 9999
        if is_done(tmp):
          return 1
        else:
          b = 1 + visit2(cnt+1, tmp)
        if b < rtv: rtv = b
    if 0 < n:
      tmp = list(arr1)
      a = paint(n, arr1[n-1], tmp)
      if a:
        b = 9999
        if is_done(tmp):
          return 1
        else:
          b = 1 + visit2(cnt+1, tmp)
        if b < rtv: rtv = b
  if key in dp:
    if rtv < dp[key]: dp[key] = rtv
    # print("replaced ", key, ' => ', dp[key])
  else:
    dp[key] = rtv
    # print("cached ", key, ' => ', dp[key])
  return rtv

## TDD
# test = [1,1,2,2,3,3,3,2,2,1,1]
# N = len(test)
# print(test)
# # paint(3,3,test)
# best_ans = visit2(0, test)
# print(test)

## TDD
# if is_done(arr):
#   best_ans = 0
# else:
#   ans = visit(0, arr)

best_ans = visit2(0, arr)
print(best_ans)

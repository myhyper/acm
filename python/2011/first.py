import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('i2.txt').readline
arr = f()
ch = " abcdefghijklmnopqrstuvwxyz"
def prt1(a):
  rtv = ""
  for n in a:
    rtv += prt2(n)
  return rtv
def prt2(n):
  return ch[int(n)]
dp = {}
def visit2(a):
  if a in dp: return dp[a]
  l = len(a)
  cnt = 0
  for i in range(1, l):
    n = int(a[i-1] + a[i])
    if 9 < n and n <= 26:
      c = a[i+1:l]
      cnt += 1
      cnt += visit2(c)
  if cnt:
    cnt -= 1
  dp[a] = cnt%1000000
  return cnt%1000000

def visit(a):
  l = len(a)
  cnt = 0
  if 0 == a.count('0'):
    cnt += 1
  else:
    for i in range(1, l):
      if a[i] == '0':
        if not '1' == a[i-1] and not '2' == a[i-1]:
          return 0
  for i in range(1, l):
    n = int(a[i-1] + a[i])
    if 9 < n and n <= 26:
      c = a[i+1:l]
      if '' != c:
        if '0' == c[0]:
          continue
      for _ in range(i+1+1, l):
        if '0' == a[_]:
          if not '1' == a[_-1] and not '2' == a[_-1]:
            continue
      cnt += 1
      cnt += visit2(c)
  return cnt%1000000

if '0' == arr[0]:
  print(0)
else:
  print(visit(arr))
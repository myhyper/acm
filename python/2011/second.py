import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('i1.txt').readline
arr = f()
print(arr)

M = 10
dp = [ [0 for _ in range(M)] for _ in range(M) ]

def visit(a):
  n = len(a)
  for j in range(1, n+1):
    for i in range(0, n):
      if n < i+j: continue

      for k in range(i, i+j):
        num = int(a)
        print(i,'~',i+j,':', a[i:i+j], 'inside', k)
        print(i, k, a[i:k], k, i+j, a[k:i+j])
        dp[i][i+j] = 1
  return -1

print(visit(arr))
for d in dp: print(d)
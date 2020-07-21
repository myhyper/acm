import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('24.txt').readline
N,K = map(int, f().split())
W = [0];V = [0];M=0
for _ in range(N):
  w, v = map(int, f().split())
  if w <= K:
    W.append(w);V.append(v)
    M += 1
arr = [[''] * (K+1) for _ in range(M+1)]
def visit(i, j):
  if arr[i][j] != '': return arr[i][j]
  if i == 0 or j == 0: rtv = 0
  elif j < W[i]: rtv = visit(i-1, j)
  else:
    a = visit(i-1, j)
    b = V[i] + visit(i-1, j-W[i])
    rtv = max(a, b)
  arr[i][j] = rtv
  return rtv
print(visit(M, K))
if dbg:
  for a in arr: print(a)
import sys
def fn():
  f = sys.stdin
  f = open('i.txt')
  N,K = map(int, f.readline().split())
  A = [[0]*5 for _ in range(N)]
  B = [[0]*2 for _ in range(N*50)]
  M = 0
  u = 0
  for _ in range(N):
    w,v,c = map(int, f.readline().split())
    for j in range(len(A)):
      r = A[j]
      if r[4] == v and r[3] == w:
        if r[2] * v < K:r[2] += c
        c = 0
        break
    if c:
      r = A[u]
      r[3],r[4],r[2] = w,v,c
      u+=1
  for _ in range(len(A)):
    r = A[_]
    m,w,v = r[2],r[3],r[4]
    while m:
      t = m-(m>>1)
      A[M][0],A[M][1] = w*t,v*t
      m = m >> 1
      M += 1
      if len(A) <= M:
        A += B
      if K < t: break
  dp = [0 for _ in range(K+1)]
  for i in range(M):
    r = A[i]
    w,v = r[0],r[1]
    l = r[0]-1
    for j in range(K,l,-1):
      h = dp[j-w]+v
      if dp[j] < h: dp[j] = h
  print(dp[K])
fn()
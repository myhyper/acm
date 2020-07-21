import sys
f = sys.stdin.readline
dbg = 1
method = 4
if dbg: f = open('k.txt').readline
N,K = map(int, f().split())
W = [0];V = [0]
if 1:
  arr = []
  for i in range(N):
    w,v,c = map(int,f().split())
    if w <= K:arr.append([w,v,c]) # 최적화1 w가 k보다 작아야만 고려 한다.
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i][0]:
        if arr[i][0] == arr[j][0]:
          if arr[i][1] == arr[j][1]:
            arr[i][2] += arr[j][2] #최적화2 같은무게 같은 가치는 합친다.
            if K < arr[i][0] * arr[i][2]: # 최적화3 무게*갯수 가 k를 초과 하면 갯수를 줄인다.
              if 1:
                arr[i][2] = int(K / arr[i][0])
              # 최적화4 이것만으로 가방을 채울정도므로 같은 무게의 낮은 가치는 없애버린다.
              if 1:
                for k in range(len(arr)):
                  if i!=k and arr[k][0] == arr[i][0]:
                    if arr[k][1] < arr[i][1]:
                      arr[k][2] = 0
            arr[j][2] = 0
  M = 0
  for w,v,c in arr:
    t = 1
    while c:
      M += 1 # 최적화 끝판왕. 복수를 2배수로 늘린 아이템1개로 재조합 한다.
      if t <= c:c -= t;W.append(w * t);V.append(v * t);t *= 2
      else:W.append(w * c);V.append(v * c);break
  if 0:
    for i in range(len(W)): # 최적화 5 가치순으로 정렬 
      for j in range(i+1,len(W)):
        if V[i] > V[j]:
          temp = W[i];W[i] = W[j];W[j] = temp
          temp = V[i];V[i] = V[j];V[j] = temp
  if 0:
    for i in range(len(W)): # 최적화 5 크기순으로 정렬 
      for j in range(i+1,len(W)):
        if W[i] < W[j]:
          temp = W[i];W[i] = W[j];W[j] = temp
          temp = V[i];V[i] = V[j];V[j] = temp
else: # 최적화 없는 경우
  M = 0
  for i in range(N):
    w,v,c = map(int,f().split())
    t = 1
    while c:
      M += 1
      if t <= c:c -= t;W.append(w * t);V.append(v * t);t *= 2
      else:W.append(w * c);V.append(v * c);break

if 1==method:
  dp = [ [ 0 for _ in range(K+1) ] for _ in range(M+1) ]
  for i in range(1, M+1):
    for j in range(1, K+1):
      if W[i] <= j and W[i] <= K:
        dp[i][j] = max(dp[i-1][j-W[i]] + V[i], dp[i-1][j])
      else:
        dp[i][j] = dp[i-1][j]
  print(dp[M][K])
if 11==method:
  dp1 = [ 0 for _ in range(K+1) ]
  dp2 = [ 0 for _ in range(K+1) ]
  for i in range(1, M+1):
    for j in range(1, K+1):
      now = dp1;prev = dp2
      if i%2 ==0: prev = dp1;now = dp2
      if W[i] <= j and W[i] <= K:
        now[j] = max(prev[j-W[i]] + V[i], prev[j])
      else:
        now[j] = prev[j]
  print(max(dp1[K], dp2[K]))

if 2==method:
  # prt = 0
  dp1 = [ 0 for _ in range(K+1) ]
  dp2 = [ 0 for _ in range(K+1) ]
  def foo():
    for i in range(len(V)):
      # if prt: print(i)
      now = dp1;prev = dp2
      if i%2 ==0: prev = dp1;now = dp2
      w = W[i];v = V[i]
      if w <= K: now[w] = max(prev[w],v) # 새로운 가능성 점화
      for j in range(K+1): # <- 배운점: K+1 이어야 했다. K에 딱맞는 비싼 물건 이 있을시. (j.txt 9째줄)
        now[j] = max(now[j], prev[j])
        if 0 < prev[j] and j+w <= K:
          now[j+w] = max(prev[j+w], prev[j]+v) # 앞에서 잇는 경우
      # if prt: print(prev);print(now)
  foo();print(max(max(dp1),max(dp2)))

if 3==method:
  sys.setrecursionlimit(999999)
  dp = [[-1] * (K+1) for _ in range(M+1)]
  def visit(i, j):
    if dp[i][j] != -1:
      return dp[i][j]
    if i == 0 or j == 0:
      rtv = 0
    elif j < W[i]:
      rtv = visit(i-1, j)
    else:
      a = visit(i-1, j)
      b = V[i] + visit(i-1, j-W[i])
      rtv = max(a, b)
    dp[i][j] = rtv
    return rtv
  print(visit(M, K))

if 4==method:
  def foo():
    dp = [0] * (K + 1)
    for i in range(M+1):
      for j in range(K, 0, -1):
        if W[i] <= j:
          dp[j] = max(dp[j], dp[j - W[i]] + V[i])
        else:
          break
    print(dp[-1])
    return
  foo()
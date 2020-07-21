import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('i.txt').readline
N,K = map(int, f().split())
W = [0];V = [0]
if 1:
  arr = []
  for i in range(N):
    w,v,c = map(int,f().split())
    if w <= K:arr.append([w,v,c]) # 최적화1
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i][0]:
        if arr[i][0] == arr[j][0]:
          if arr[i][1] == arr[j][1]:
            arr[i][2] += arr[j][2] #최적화2
            if K < arr[i][0] * arr[i][2]: # 최적화3
              if 1:
                arr[i][2] = int(K / arr[i][0])
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
if 1:
  dp = [0] * (K + 1)
  for i in range(M+1):
    for j in range(K, 0, -1):
      if W[i] <= j:
        dp[j] = max(dp[j], dp[j - W[i]] + V[i])
      else:
        break
  print(dp[-1])
import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('37.txt').readline
N, K = map(int, f().split())
arr = [ [0, 0] for _ in range(N) ]
for n in range(N): arr[n] = map(int, f().split())
dp1 = [K];dp2 = [0] # DP초기값

def put(w, v):
  if w < 0: return # 남은무게 w -> v 값어치. 무게는 음수불가
  if w in dp1:
    i = dp1.index(w)
    if dp2[i] < v:
      dp2[i] = v # 더 나은 후보 발견
      print(w,'*=>',v)
  else:
    dp1.append(w);dp2.append(v) # 메모이제이션 
    print(w,'=>',v)

def visit(idx):
  w,v = arr[idx]
  for room, val in zip(list(dp1), list(dp2)):
    put(room-w, val+v)
for i in range(N): visit(i)

# for x,y in zip(dp1,dp2): print(x,'=>',y)
print(max(dp2))
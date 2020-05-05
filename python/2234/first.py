import sys
sys.setrecursionlimit(999999)
f = sys.stdin.readline
dbg = 1
if dbg: f = open('input4.txt').readline
C,R = map(int,f().split())
arr = []
for r in range(R):
  arr.append(list(map(int,f().split())))
  # for c in range(C):
  #   if c & 0b0001: print('1')
  #   if c & 0b0010: print('2')
  #   if c & 0b0100: print('3')
  #   if c & 0b1000: print('4')
# print(arr)
tmp = [[0 for _ in range(C)] for _ in range(R)]
m_lv = [[0 for _ in range(C)] for _ in range(R)]
max_lv = [0, 0]
def visit(x,y, cnt, lv):
  global max_lv
  if tmp[y][x]: return -1
  tmp[y][x] = cnt
  m_lv[y][x] = lv
  if max_lv[cnt] < lv: max_lv[cnt] = lv
  c = arr[y][x]
  if not (c & 0b0001) and 0 < x:
    rtv = visit(x-1,y, cnt, lv+1)
    if 0 < rtv: lv = rtv
  if not (c & 0b0010) and 0 < y:
    rtv = visit(x,y-1, cnt, lv+1)
    if 0 < rtv: lv = rtv
  if not (c & 0b0100) and x < C-1:
    rtv = visit(x+1,y, cnt, lv+1)
    if 0 < rtv: lv = rtv
  if not (c & 0b1000) and y < R-1:
    rtv = visit(x,y+1, cnt, lv+1)
    if 0 < rtv: lv = rtv
  return lv
cnt = 1
def visit2(x,y):
  rtv = 0
  c = arr[y][x]
  if (c & 0b0001) and 0 < x:
    if tmp[y][x] != tmp[y][x-1]:
      a = max_lv[tmp[y][x]] + max_lv[tmp[y][x-1]]
      if rtv < a: rtv = a
  if (c & 0b0010) and 0 < y:
    if tmp[y][x] != tmp[y-1][x]:
      a = max_lv[tmp[y][x]] + max_lv[tmp[y-1][x]]
      if rtv < a: rtv = a
  if (c & 0b0100) and x < C-1:
    if tmp[y][x] != tmp[y][x+1]:
      a = max_lv[tmp[y][x]] + max_lv[tmp[y][x+1]]
      if rtv < a: rtv = a
  if (c & 0b1000) and y < R-1:
    if tmp[y][x] != tmp[y+1][x]:
      a = max_lv[tmp[y][x]] + max_lv[tmp[y+1][x]]
      if rtv < a: rtv = a
  return rtv
for r in range(R):
  for c in range(C):
    rtv = visit(c,r, cnt, 1)
    if -1 != rtv:
      max_lv.append(0)
      cnt += 1
ans = 0
for r in range(R):
  for c in range(C):
    rtv = visit2(c,r)
    if ans < rtv: ans = rtv
if dbg:
  for r in range(R):
    print(m_lv[r])
print(cnt-1)
if dbg: print(max_lv)
print(max(max_lv))
print(ans)
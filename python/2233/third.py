import sys
f = sys.stdin.readline
dbg = 0
prt = 0
if dbg: f = open('input4.txt').readline

N = int(f())
arr = f().strip()
a,b = map(int,f().split())

class Apple:
  n_lv = 0
  n_root = None
  n_left = None
  n_right = None
  def __init__(self, root=None):
    self.n_root = root
  cnt_in = None
  cnt_out = None

virtual_root = Apple()
objs = [ virtual_root ]
now = virtual_root
cnt = 1
tot = 1
lv = 0
for n in arr:
  if '0' == n:
    lv += 1
    if not now.n_left:
      now.n_left = Apple(now)
      objs.append(now.n_left)
      now = now.n_left
    else:
      now.n_right = Apple(now)
      objs.append(now.n_right)
      now = now.n_right
    now.cnt_in = cnt
    now.n_idx = tot
    now.n_lv = lv
    tot += 1
    if prt:
      for _ in range(lv-1):
        print('\t',end='')
      print(cnt, '=>', '[', now.n_idx, ']')
    if a == cnt: x = now
    if b == cnt: y = now
  else:
    if a == cnt: x = now
    if b == cnt: y = now
    lv -= 1
    now.cnt_out = cnt
    if prt:
      for _ in range(lv):
        print('\t',end='')
      print('<=', cnt, '[', now.n_idx, ']')
    now = now.n_root
  cnt += 1

# print(x.n_idx, y.n_idx)
while x.n_lv < y.n_lv: y = y.n_root
while y.n_lv < x.n_lv: x = x.n_root
while x is not y:
  y = y.n_root
  x = x.n_root
print(x.cnt_in, x.cnt_out)
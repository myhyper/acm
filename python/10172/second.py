import sys
f = sys.stdin.readline
T = int(f())
for t in range(T):
  x,y=map(int,f().split())
  tar = y-x
  s=0
  spd=1
  m=1
  n=0
  while s < tar:
    s+= spd
    print('spd',spd)
    if not s < tar: break
    s+= spd
    print('spd',spd)
    spd+=1

  print(spd)
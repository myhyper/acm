import sys
import math
T = int(sys.stdin.readline())
for t in range(T):
  x, y = [int(k) for k in sys.stdin.readline().split()]
  d = y - x
  if d < 3:
    print(d)
  else:
    p = int(math.sqrt(d))
    if d > p*(p + 1):
      p += 1
    if d > p*p:
      p *= 2
    else:
      p = p * 2 - 1
    print(p)
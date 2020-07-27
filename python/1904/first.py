import math
M=15746
N=int(input())
def sigma(n):
  rtv = 0
  for i in range(n):
    rtv += i
  return rtv
arr=[0 for _ in range(N)]
def foo(n):
  if n <= 1: return 0
  if n == 2: return 2
  if n == 3: return 3
  a = sigma(n-3)
  b = 0
  for i in range(n-3):
    b *= 2
    b %= M
    if 0 == b: b = 1
  # return (n + a + int(math.pow(2,n-4) % M)) % M
  return (n + a + int(b % M)) % M
  return b
print(foo(N))


# 3 -> 3 (3+0) 
# 111
# 001
# 100

# 4 -> 5 (4+1)
# 11 11
# 00 11
# 10 01 < 11 11
# 11 00
# 00 00

# 5 -> 8 (6+2)
# 11 111
# 11 001
# 11 100
# 10 011 < 11 111
# 10 000 < 11 100
# 00 111
# 00 001
# 00 100


# 6 -> 13 (9+4)
# 111 111
# 001 111
# 100 111
# 110 011 < 111 111
# 111 001
# 111 100
# 000 011 < 001 111
# 001 001
# 001 100
# 100 001
# 100 100
# 110 000 < 111 100
# 000 000 < 001 100

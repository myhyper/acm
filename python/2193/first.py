import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('i.txt').readline
N = int(f())
if 1:
  def foo(n, last):
    if n == 1:
      return 1
    a = foo(n-1, 0)
    b = foo(n-1, 1)
    return a + b
  a = foo(N-1, 0)
  b = foo(N-1, 1)
  print(ans)
import sys
f = sys.stdin.readline
N = int(f())
st = ''
for n in range(2,N):
  def foo(num):
    if num > 1:
      for i in range(2, num//2):
        if (num % i) == 0:
          #print(num, "is not a prime number")
          return 0
        else:
          #print(num, "is a prime number")
    else:
      #print(num, "is not a prime number")
      return 0
    return 1
  if foo(n):
    if st != '':
      st += ','
    st += "%d" % (n)
print(st)
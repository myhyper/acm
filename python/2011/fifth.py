import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('8.txt').readline
arr = f()
M = 10
dp = [ 0 for _ in range(M)]

def foo():
  jump = ''
  prev = ''
  for i in range(len(arr)):
    c = arr[i]

    n = prev + c

    a = 1

    if '' == prev and '0' == c: return 0

    if '09' < n and n < '27':
      if '10' == n or n == '20':
        a = dp[(i-2)%M]
        if not a: a = 1
        print('A')
      else:
        a = dp[(i-2)%M] * dp[(i-1)%M]
        st = arr[i-2] + arr[i-1]
        if '09' < st and st < '27':
          p = dp[(i-1)%M]
          a = dp[(i-2)%M] * dp[(i-1)%M] - int(dp[(i-1)%M] / 2)
        print('B')
        if a <= 1:
          if dp[(i-2)%M] == 0 and 0 == dp[(i-1)%M]:
            print('B1')
            a = 1
          elif dp[(i-2)%M] == 1 and 1 == dp[(i-1)%M]:
            print('B2')
            a = 2
          else:
            print('B3')
            a = 2
    elif '0' < c and c <= '9':
      print('C')
      a = dp[(i-1)%M]
    else:
      a = 0

    print(n, '=>', a)

    dp[i%M] = a % 1000000

    jump = prev
    prev = c
  return dp[(len(arr)-1)%M]
a = foo()
print(a)
print(dp)

# 2 5 1 1 4
# 25 1 1 4
# 2 5 11 4
# 25 11 4

# 2 5 1 14
# 25 1 14
# 2 5 114 x
# 25 114 x

import sys
f = sys.stdin.readline
dbg = 1
prt = 0
if dbg: f = open('i4.txt').readline
arr = f()
M = 5001
dp = [ 0 for _ in range(M)]

def foo():
  for i in range(len(arr)):
    def f1():
      if '0' == arr[i]: return False # 한자리가 0이면 안합칠 수가 없다.
      a = arr[i-1]
      if '0' <= a and a <= '9':
        b = arr[i]
        if '0' <= b and b <= '9':
          return True
      return False
    def f2():
      if 0 == i: return False # 0번째 인덱스면 합칠 수가 없다.
      a = arr[i-1] + arr[i]
      if '09' < a and a < '27':
        return True
      return False
    ch = arr[i]
    def prev(): # 앞번 dp를 꺼내온다.
      if 0 == i: return 1
      return dp[(i-1)%M]
    def preprev(): # 앞앞 dp를 꺼내온다.
      if i <= 1: return 1
      return dp[(i-2)%M]
    tmp = 0
    if f1() and not f2(): # 안합칠수밖에 없는 경우
      dp[i%M] = prev()
      tmp = 1
    elif not f1() and f2(): # 합칠 수 밖에 없는 경우
      dp[i%M] = preprev()
      tmp = 2
    elif f1() and f2(): # 둘다 가능 한 경우
      dp[i%M] = (prev() + preprev()) % 1000000
      tmp = 3
    else: # 둘다 불가능 한경우 = 답0
      return 0
    if prt: print(ch, '=>', tmp)
  return dp[(len(arr)-1)%M]
a = foo()
print(a)
if prt: print(dp)
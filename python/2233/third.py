import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('input.txt').readline

N = int(f())
arr = f()
a,b = map(int,f().split())
print(a,b)

for ch in arr:
  if '0' == ch:
  elif '1' == ch:
  else:
    break
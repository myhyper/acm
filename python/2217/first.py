import sys
f = sys.stdin.readline
# dbg = True
# if dbg: f = open('input.txt').readline
T  = int(f())
arr = [10000 for _ in range(T)]
for t in range(T):
    arr[t] = int(f())

arr.sort()
last = arr[0]
ans = last * (T - 0)
for i in range(T):
    if last == arr[i]: continue
    last = arr[i]
    if ans < last * (T - i):
        ans = last * (T - i)
print(ans)
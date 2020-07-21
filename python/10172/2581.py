import sys
M=0xf4240;e=[1 for i in range(M)]
for i in range(2,M):
  for j in range(i,M,i):
    if j==i:continue
    else:e[j]=0
e[1]=0;f=sys.stdin.readline
while 1:
  n=int(f())
  if n:print(sum(e[n+1:2*n+1]))
  else:break
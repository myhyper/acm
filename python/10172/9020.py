ps = [0] + [1] * 246911
for _ in range(2, 497):
  i = _ - 1
  if ps[i]:
    for j in range(i + _, 246912, _):
      ps[j] = 0
T=int(input())
for t in range(T):
  n=int(input())
  z=x=y=n
  for i in range(n):
    for j in range(n):
      if n < i+j: break
      if ps[i+1] and ps[j+1] and i+j==n:
        if abs(i-j) < z: z=abs(i-j);x=i;y=j
  print(x,y)
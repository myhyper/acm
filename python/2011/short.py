a=[0]+list(map(int,input()))
n=len(a)
d=[[0]*2 for i in range(5001)]
d[0][1]=1
for i in range(1,n):
  if a[i]==0:d[i][1]=0
  else:d[i][1]=d[i-1][1]+d[i-1][0]
  if(a[i-1]==1 and 0<=a[i]<=9)or(a[i-1]==2 and 0<=a[i]<7):d[i][0]=d[i-2][1]+d[i-2][0]
print((d[n-1][1]+d[n-1][0])%0xF4240)

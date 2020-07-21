import sys
if 1:
  def e():
    f=sys.stdin
    N,K=map(int,f.readline().split())
    B=[[0]*2 for _ in range(N*24)]
    def q():
      u=M=0;A=[[0]*3 for _ in range(N)]
      for _ in range(N):
        w,v,c=map(int,f.readline().split())
        for j in range(u):
          r=A[j]
          if r[1]==v and r[0]==w:
            if r[1]*v<K:r[2]+=c
            c=0;break
        if c:A[u]=[w,v,c];u+=1
      A.sort(reverse=1)
      for _ in range(N):
        w,v,m=A[_]
        while m:t=m;m>>=1;t-=m;B[M]=w*t,v*t;M+=1
      return M
    def g():
      d=[0 for _ in range(K+1)]
      for i in range(M):
        w,v=B[i];l=w-1
        for j in range(K,l,-1):
          h=d[j-w]+v
          if d[j]<h:d[j]=h
      print(d[K])
    M=q();g()
  e()
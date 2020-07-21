import sys
f = sys.stdin.readline
T = int(f())
ans=[0 for _ in range(50)]
for _ in range(T):
  arr = list(map(int,f().split()))
  x,y = arr[0],arr[1]
  tar = y-x
  for tar in range(1,200):
    dp=[]
    for i in range(tar):
      def foo():
        for j in range(len(dp)-2,0,-1):
          if dp[j-1] == dp[j] == dp[j+1]:
            dp[j] += 1
            return 1
          if dp[j-1]-1 == dp[j] == dp[j+1]:
            dp[j] += 1
            return 1
        return 0
      if not foo():
        dp.append(1)
      #print(dp,sum(dp))
    ans[len(dp)] += 1
    #print(tar,len(dp))
print(ans)

#  1 1  1
#  2 2  1 1
#  3 3  1 1 1
#  4 3  1 2 1
#  5 4  1 2 1 1
#  6 4  1 2 2 1
#  7 5  1 2 2 1 1
#  8 5  1 2 2 2 1
#  9 5  1 2 3 2 1
# 10 6  1 2 3 2 1 1
# 11 6  1 2 3 2 2 1
# 12 6  1 2 3 3 2 1
# 13 7  1 2 3 3 2 1 1


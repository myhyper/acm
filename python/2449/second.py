import sys
f = sys.stdin.readline
dbg = 0
if dbg: f = open('input2.txt').readline

N,K = map(int, f().split())
arr = list(map(int, f().split()))
# print(arr)

# UTIL: 압축을 한다 ex) 11333 -> 13
def press(arr, ptn):
  counts = [ 0 for _ in range(21) ]
  for i in range(len(arr)-1, 0, -1):
    if arr[i] == arr[i-1]:
      arr.pop(i)
  while len(arr) != len(ptn):
    ptn.pop(-1)
  a = 1
  for i in range(len(arr)):
    counts[arr[i]] += 1
  a = 1
  for i in range(len(arr)):
    ptn[i] = counts[arr[i]]
  a = 1

# TDD
a = [0,2,2]
b = [0,2,2]
press(a,b)
if [1,1] != b: print("ERR 1", a)
a = [0,0,0,1,1,1,1,2,2,2]
b = [0,0,0,1,1,1,1,2,2,2]
press(a,b)
if [1,1,1] != b: print("ERR 2", a)
a = [3,3,3,4,4,4,4,5,5,5]
press(a,b)
if [1,1,1] != b: print("ERR 3", a)
a = [3,3,3,5,5,5,5,8,8,8]
press(a,b)
if [1,1,1] != b: print("ERR 4", a)

ptn = list(arr)
press(arr,ptn)
# print(arr)

def count_number_of_1(arr):
  rtv = 0
  for i in arr:
    if 1 == i:
      rtv += 1
  return rtv
if count_number_of_1([1,1,1]) != 3: print("ERR 10")

def remove_all_of_1(arr):
  rtv = 0
  for i in range(len(arr)-1, 0, -1):
    if arr[i] == 1 and 1 == arr[i-1]:
      rtv += 1
      arr.pop(i)
  return rtv
a = [1,1,1]
r = remove_all_of_1(a)
if r != 2: print("ERR 11", r)
if a != [1]: print("ERR 12", a)


dp = {}

def visit(ar, ptn):
  if 0 == len(ar):
    return 0
  if 1 == len(ar):
    return 0
  if 2 == len(ar):
    return 1
  key = str(ptn)
  if key in dp:
    return dp[key]
  min_cnt = 9999
  for i in range(len(ar)):
    tmp = list(ar)
    tmp.pop(i)
    p = list(tmp)
    press(tmp, p)
    no1 = count_number_of_1(p)
    if no1 == len(p):
      rtv = no1 - 1
    else:
      remove = remove_all_of_1(p)
      rtv = visit(tmp, p) + remove
    if 9999 == min_cnt: min_cnt = rtv
    if rtv < min_cnt: min_cnt = rtv
  if key in dp:
    if min_cnt + 1 < dp[key]:
      dp[key] = min_cnt + 1
  else:
    dp[key] = min_cnt + 1
  return min_cnt + 1

ans = visit(arr, ptn)
print(ans)
print(dp)
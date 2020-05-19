import sys
DEBUG = True
# DEBUG = False
if DEBUG:
  f = open("i4.txt")
else:
  f = sys.stdin
# function
def is_alphameric_range(prev,curr):
  ans = (10*prev) + curr
  if ans >= 10 and ans <= 26:
    return True
  else:
    return False
# input
input_data = f.readline().strip()
# array input
encode_arr = [int(_) for _ in input_data]
encode_len = len(encode_arr)
# dp
one = [0 for _ in range(encode_len+100)]
two = [0 for _ in range(encode_len+100)]
dp = [0 for _ in range(encode_len+100)]
# base case
one[1] = 1
two[1] = 0  
dp[0] = 1
dp[1] = 1
def visit():
  # exception
  if not len(encode_arr) or not encode_arr[0]:
    print("0")
    return
  # logic
  for idx in range(1, encode_len):
    # one
    if encode_arr[idx] == 0:
      one[idx+1] = 0
    else:
      one[idx+1] = dp[idx]
    # two
    if encode_arr[idx] == 0 and (encode_arr[idx-1] != 1 and encode_arr[idx-1] != 2):
      print("0")
      return
    if is_alphameric_range(encode_arr[idx-1], encode_arr[idx]):
      two[idx+1] = dp[idx-1]
    else:
      two[idx+1] = 0
    #result
    dp[idx+1] = one[idx+1] + two[idx+1]
  print(dp[encode_len] % 1000000)
  return
visit()

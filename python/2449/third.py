# 모든 숫자가 같아 지기 위한 비용
# 1 => 0

# 2
# [1,2] => 1
# [1,1] => 0

# 3
# [1,1,1] => 0
# [2,1,1] => 1
# [1,2,1] => 1
# [1,1,2] => 1
# [2,1,2] => 1
# [1,2,3] => 2

# 4
import sys
sys.setrecursionlimit(999999)
f = sys.stdin.readline
dbg = 0
if dbg: f = open('input.txt').readline

if dbg:
  import random

dp = {'[1, 2, 3]': 2, '[1, 2, 1]': 1, '[1, 2, 2, 2, 2, 1]': 1, '[1, 2, 2, 2, 1]': 1, '[1, 2, 2, 1]': 1, '[2, 2, 2, 2, 1]': 1, '[2, 2, 2, 1]': 1, '[2, 2, 1]': 1, '[1, 2, 3, 3, 2, 2, 1]': 2, '[1, 2, 3, 3, 2, 1]': 5, '[1, 2, 3, 2, 2, 1]': 2, '[1, 2, 3, 2, 1]': 3, '[1, 3, 3, 2, 2, 1]': 2, '[1, 3, 3, 2, 1]': 4, '[1, 3, 2, 2, 1]': 2, '[1, 3, 2, 1]': 2, '[2, 3, 3, 2, 2, 1]': 2, '[2, 3, 3, 2, 1]': 4, '[2, 3, 2, 2, 1]': 2, '[2, 3, 2, 1]': 2, '[3, 3, 2, 2, 1]': 2, '[3, 3, 2, 1]': 3, '[3, 2, 2, 1]': 2, '[3, 2, 1]': 2, '[1, 1, 2, 3, 3, 3, 2, 2, 1, 1]': 2, '[1, 1, 2, 3, 3, 3, 2, 1, 1]': 7, '[1, 1, 2, 3, 3, 3, 1, 1]': 6, '[1, 1, 2, 3, 3, 2, 2, 1, 1]': 4, '[1, 1, 2, 3, 3, 2, 1, 1]': 6, '[1, 1, 2, 3, 3, 1, 1]': 5, '[1, 1, 2, 3, 2, 2, 1, 1]': 4, '[1, 1, 2, 3, 2, 1, 1]': 5, '[1, 1, 2, 3, 1, 1]': 4, '[1, 1, 2, 2, 2, 1, 1]': 3, '[1, 1, 2, 2, 1, 1]': 3, '[1, 1, 2, 1, 1]': 3, '[1, 1, 3, 3, 3, 2, 2, 1, 1]': 4, '[1, 1, 3, 3, 3, 2, 1, 1]': 6, '[1, 1, 3, 3, 3, 1, 1]': 5, '[1, 1, 3, 3, 2, 2, 1, 1]': 4, '[1, 1, 3, 3, 2, 1, 1]': 5, '[1, 1, 3, 3, 1, 1]': 4, '[1, 1, 3, 2, 2, 1, 1]': 4, '[1, 1, 3, 2, 1, 1]': 4, '[1, 1, 3, 1, 1]': 3, '[1, 1, 1, 1]': 2, '[1, 2, 3, 3, 3, 2, 2, 1, 1]': 2, '[1, 2, 3, 3, 3, 2, 1, 1]': 6, '[1, 2, 3, 3, 3, 1, 1]': 5, '[1, 2, 3, 3, 2, 2, 1, 1]': 2, '[1, 2, 3, 3, 2, 1, 1]': 5, '[1, 2, 3, 3, 1, 1]': 4, '[1, 2, 3, 2, 2, 1, 1]': 2, '[1, 2, 3, 2, 1, 1]': 4, '[1, 2, 3, 1, 1]': 3, '[1, 2, 2, 2, 1, 1]': 1, '[1, 2, 2, 1, 1]': 1, '[1, 2, 1, 1]': 1, '[1, 3, 3, 3, 2, 2, 1, 1]': 2, '[1, 3, 3, 3, 2, 1, 1]': 5, '[1, 3, 3, 3, 1, 1]': 4, '[1, 3, 3, 2, 2, 1, 1]': 2, '[1, 3, 3, 2, 1, 1]': 4, '[1, 3, 3, 1, 1]': 3, '[1, 3, 2, 2, 1, 1]': 2, '[1, 3, 2, 1, 1]': 3, '[1, 3, 1, 1]': 2, '[1, 1, 1]': 0, '[2, 3, 3, 3, 2, 2, 1, 1]': 2, '[2, 3, 3, 3, 2, 1, 1]': 5, '[2, 3, 3, 3, 1, 1]': 4, '[2, 3, 3, 2, 2, 1, 1]': 2, '[2, 3, 3, 2, 1, 1]': 4, '[2, 3, 3, 1, 1]': 3, '[2, 3, 2, 2, 1, 1]': 2, '[2, 3, 2, 1, 1]': 3, '[2, 3, 1, 1]': 2, '[2, 2, 2, 1, 1]': 1, '[2, 2, 1, 1]': 1, '[2, 1, 1]': 1, '[3, 3, 3, 2, 2, 1, 1]': 2, '[3, 3, 3, 2, 1, 1]': 4, '[3, 3, 3, 1, 1]': 3, '[3, 3, 2, 2, 1, 1]': 2, '[3, 3, 2, 1, 1]': 3, '[3, 3, 1, 1]': 2, '[3, 2, 2, 1, 1]': 2, '[3, 2, 1, 1]': 2, '[3, 1, 1]': 1, '[1, 1, 2, 3, 4, 3, 2, 2, 1, 1]': 3, '[1, 1, 2, 3, 4, 3, 2, 1, 1]': 7, '[1, 1, 2, 3, 4, 2, 2, 1, 1]': 6, '[1, 1, 2, 3, 4, 2, 1, 1]': 6, '[1, 1, 2, 4, 3, 2, 2, 1, 1]': 5, '[1, 1, 2, 4, 3, 2, 1, 1]': 6, '[1, 1, 2, 4, 2, 2, 1, 1]': 5, '[1, 1, 2, 4, 2, 1, 1]': 5, '[1, 1, 3, 4, 3, 2, 2, 1, 1]': 5, '[1, 1, 3, 4, 3, 2, 1, 1]': 6, '[1, 1, 3, 4, 2, 2, 1, 1]': 5, '[1, 1, 3, 4, 2, 1, 1]': 5, '[1, 1, 4, 3, 2, 2, 1, 1]': 5, '[1, 1, 4, 3, 2, 1, 1]': 5, '[1, 1, 4, 2, 2, 1, 1]': 4, '[1, 1, 4, 2, 1, 1]': 4, '[1, 2, 3, 4, 3, 2, 2, 1, 1]': 3, '[1, 2, 3, 4, 3, 2, 1, 1]': 6, '[1, 2, 3, 4, 2, 2, 1, 1]': 5, '[1, 2, 3, 4, 2, 1, 1]': 5, '[1, 2, 4, 3, 2, 2, 1, 1]': 3, '[1, 2, 4, 3, 2, 1, 1]': 5, '[1, 2, 4, 2, 2, 1, 1]': 4, '[1, 2, 4, 2, 1, 1]': 4, '[1, 3, 4, 3, 2, 2, 1, 1]': 3, '[1, 3, 4, 3, 2, 1, 1]': 5, '[1, 3, 4, 2, 2, 1, 1]': 4, '[1, 3, 4, 2, 1, 1]': 4, '[1, 4, 3, 2, 2, 1, 1]': 3, '[1, 4, 3, 2, 1, 1]': 4, '[1, 4, 2, 2, 1, 1]': 3, '[1, 4, 2, 1, 1]': 3, '[3, 1, 3]': 1, '[1, 1, 3]': 1, '[3, 2, 3]': 1, '[2, 3, 2]': 1, '[1, 2, 2]': 1, '[2, 1, 3]': 2, '[1, 3, 1]': 1, '[3, 2, 2]': 1, '[1, 1, 2]': 1, '[2, 3, 1]': 2, '[3, 1, 2]': 2, '[2, 1, 2]': 1, '[2, 1, 2, 1]': 2, '[3, 1, 3, 2]': 2, '[1, 3, 2]': 2, '[2, 3, 1, 2]': 2, '[2, 1, 2, 3]': 2, '[3, 2, 3, 1]': 2, '[1, 3, 2, 3]': 2, '[1, 2, 3, 2]': 2, '[3, 1, 4, 2]': 3, '[2, 1, 3, 2]': 2, '[3, 4, 1, 2]': 3, '[1, 2, 1, 2]': 2, '[1, 2, 1, 3]': 2, '[2, 3, 4, 1]': 3, '[1, 2, 4, 3]': 3, '[2, 3, 1, 3]': 2, '[2, 1, 3, 1]': 2, '[2, 3, 1, 4]': 3, '[3, 2, 1, 3]': 2, '[1, 3, 1, 2]': 2, '[4, 1, 2, 3]': 3, '[3, 4, 2, 1]': 3, '[4, 2, 3, 1]': 3, '[1, 2, 3, 4]': 3, '[3, 1, 2, 3]': 2, '[3, 2, 4, 1]': 3, '[3, 1, 2, 1]': 2, '[2, 1, 4, 3]': 3, '[1, 2, 3, 1]': 2, '[4, 2, 1, 3]': 3, '[2, 1, 3, 4]': 3, '[3, 2, 1, 2]': 2, '[4, 3, 1, 2]': 3, '[3, 1, 2, 4]': 3, '[4, 1, 3, 2]': 3, '[1, 4, 3, 2]': 3, '[2, 4, 3, 1]': 3, '[2, 4, 1, 3]': 3, '[1, 3, 2, 4]': 3, '[3, 2, 1, 4]': 3, '[1, 3, 4, 2]': 3, '[4, 3, 2, 1]': 3, '[1, 4, 2, 3]': 3, '[4, 3, 2, 1, 5]': 4, '[3, 5, 2, 4, 1]': 4, '[1, 5, 2, 4, 3]': 4, '[5, 3, 1, 4, 2]': 4, '[1, 2, 4, 3, 5]': 4, '[3, 2, 1, 2, 1]': 3, '[3, 1, 2, 4, 5]': 4, '[1, 4, 2, 5, 3]': 4, '[4, 2, 4, 1, 3]': 3, '[4, 1, 3, 2, 3]': 3, '[4, 1, 3, 5, 2]': 4, '[1, 5, 2, 3, 4]': 4, '[4, 2, 1, 3, 4]': 3, '[4, 2, 3, 5, 1]': 4, '[2, 5, 3, 4, 1]': 4, '[3, 5, 2, 1, 4]': 4, '[4, 5, 1, 2, 3]': 4, '[1, 4, 2, 1, 3]': 3, '[1, 4, 2, 3, 5]': 4, '[4, 1, 2, 3, 4]': 3, '[5, 1, 3, 2, 4]': 4, '[2, 3, 1, 5, 4]': 4, '[3, 2, 1, 3, 2]': 3, '[1, 2, 5, 4, 3]': 4, '[4, 3, 1, 2, 4]': 3, '[2, 1, 2, 1, 2]': 2, '[1, 3, 1, 4, 2]': 3, '[5, 4, 3, 2, 1]': 4, '[4, 5, 2, 1, 3]': 4, '[3, 2, 1, 4, 5]': 4, '[3, 2, 5, 1, 4]': 4, '[4, 1, 5, 3, 2]': 4, '[2, 4, 1, 3, 5]': 4, '[4, 3, 2, 3, 1]': 3, '[4, 2, 4, 3, 1]': 3, '[3, 2, 4, 1, 5]': 4, '[1, 3, 2, 1, 4]': 3, '[2, 4, 1, 3, 4]': 3, '[1, 3, 2, 1, 3]': 3, '[2, 3, 2, 1, 2]': 2, '[1, 3, 2, 4, 3]': 3, '[2, 4, 1, 3, 2]': 3, '[1, 3, 5, 2, 4]': 4, '[1, 4, 5, 3, 2]': 4, '[2, 4, 3, 5, 1]': 4, '[3, 1, 3, 2, 4]': 3, '[4, 2, 3, 1, 5]': 4, '[5, 3, 1, 2, 4]': 4, '[3, 1, 2, 4, 1]': 3, '[3, 4, 2, 1, 4]': 3, '[2, 4, 3, 4, 1]': 3, '[1, 3, 2, 1, 2]': 3, '[2, 3, 4, 1, 2]': 3, '[2, 3, 1, 4, 3]': 3, '[5, 3, 4, 1, 2]': 4, '[3, 2, 4, 1, 2]': 3, '[3, 1, 4, 1, 2]': 3, '[3, 4, 5, 1, 2]': 4, '[5, 4, 3, 1, 2]': 4, '[1, 4, 2, 3, 4]': 3, '[2, 4, 3, 1, 5]': 4, '[1, 3, 4, 5, 2]': 4, '[4, 2, 3, 1, 4]': 3, '[3, 1, 2, 4, 3]': 3, '[2, 1, 5, 3, 4]': 4, '[3, 5, 1, 2, 4]': 4, '[1, 4, 5, 2, 3]': 4, '[2, 1, 4, 5, 3]': 4, '[2, 1, 3, 2, 4]': 3, '[4, 5, 3, 1, 2]': 4, '[3, 4, 1, 5, 2]': 4, '[4, 3, 1, 3, 2]': 3, '[1, 2, 3, 4, 3]': 3, '[3, 4, 5, 2, 1]': 4, '[2, 3, 5, 4, 1]': 4, '[4, 2, 3, 1, 2]': 3, '[1, 2, 3, 1, 4]': 3, '[4, 3, 1, 4, 2]': 3, '[4, 2, 5, 1, 3]': 4, '[2, 1, 4, 3, 2]': 3, '[1, 2, 1, 2, 1]': 2, '[4, 1, 2, 4, 3]': 3, '[2, 4, 3, 1, 4]': 3, '[2, 3, 4, 1, 4]': 3, '[4, 2, 3, 1, 3]': 3, '[3, 1, 5, 4, 2]': 4, '[3, 1, 2, 1, 3]': 3, '[2, 5, 1, 3, 4]': 4, '[3, 5, 4, 2, 1]': 4, '[3, 2, 4, 2, 1]': 3, '[3, 1, 4, 3, 2]': 3, '[2, 5, 3, 1, 4]': 4, '[4, 3, 2, 1, 3]': 3, '[3, 2, 3, 1, 4]': 3, '[1, 4, 3, 5, 2]': 4, '[5, 4, 2, 1, 3]': 4, '[5, 2, 3, 4, 1]': 4, '[2, 3, 1, 2, 3]': 3, '[2, 3, 2, 4, 1]': 3, '[1, 3, 4, 2, 4]': 3, '[5, 1, 2, 3, 4]': 4, '[2, 3, 1, 4, 5]': 4, '[2, 4, 3, 2, 1]': 3, '[5, 1, 2, 4, 3]': 4, '[3, 2, 1, 2, 3]': 3, '[2, 1, 2, 3, 4]': 3, '[2, 4, 3, 1, 2]': 3, '[3, 4, 2, 1, 3]': 3, '[1, 3, 2, 3, 4]': 3, '[1, 3, 2, 3, 1]': 3, '[2, 1, 2, 4, 3]': 3, '[1, 5, 3, 4, 2]': 4, '[1, 3, 4, 2, 5]': 4, '[3, 1, 2, 1, 4]': 3, '[2, 3, 4, 1, 3]': 3, '[4, 5, 2, 3, 1]': 4, '[4, 1, 3, 2, 5]': 4, '[2, 4, 1, 3, 1]': 3, '[4, 1, 3, 2, 4]': 3, '[1, 2, 1, 3, 2]': 3, '[4, 5, 1, 3, 2]': 4, '[2, 3, 5, 1, 4]': 4, '[3, 1, 2, 5, 4]': 4, '[4, 1, 2, 3, 5]': 4, '[2, 4, 5, 1, 3]': 4, '[5, 2, 4, 1, 3]': 4, '[3, 4, 2, 1, 5]': 4, '[1, 3, 2, 4, 5]': 4, '[1, 2, 4, 1, 3]': 3, '[1, 4, 3, 2, 4]': 3, '[1, 3, 2, 3, 2]': 3, '[1, 2, 3, 5, 4]': 4, '[2, 3, 1, 3, 1]': 3, '[2, 3, 4, 1, 5]': 4, '[5, 2, 4, 3, 1]': 4, '[2, 1, 3, 4, 5]': 4, '[1, 4, 2, 3, 1]': 3, '[3, 1, 4, 2, 3]': 3, '[3, 2, 1, 2, 4]': 3, '[5, 1, 3, 4, 2]': 4, '[1, 4, 2, 3, 2]': 3, '[3, 2, 1, 4, 3]': 3, '[2, 3, 4, 2, 1]': 3, '[3, 1, 3, 2, 3]': 2, '[1, 2, 1, 3, 4]': 3, '[4, 2, 1, 2, 3]': 3, '[3, 1, 4, 2, 4]': 3, '[2, 1, 2, 1, 3]': 3, '[5, 4, 1, 2, 3]': 4, '[2, 1, 4, 3, 5]': 4, '[2, 1, 3, 4, 3]': 3, '[4, 3, 4, 2, 1]': 3, '[3, 2, 1, 5, 4]': 4, '[3, 1, 4, 2, 5]': 4, '[1, 2, 3, 1, 3]': 3, '[2, 3, 2, 1, 4]': 3, '[3, 1, 2, 3, 4]': 3, '[2, 5, 1, 4, 3]': 4, '[2, 1, 5, 4, 3]': 4, '[4, 1, 4, 2, 3]': 3, '[3, 1, 3, 4, 2]': 3, '[5, 2, 1, 4, 3]': 4, '[2, 1, 2, 3, 2]': 2, '[4, 1, 5, 2, 3]': 4, '[3, 2, 4, 5, 1]': 4, '[3, 4, 1, 2, 5]': 4, '[4, 1, 3, 1, 2]': 3, '[3, 4, 2, 5, 1]': 4, '[1, 2, 1, 4, 3]': 3, '[4, 3, 2, 5, 1]': 4, '[1, 2, 3, 4, 5]': 4, '[2, 1, 3, 1, 4]': 3, '[2, 1, 4, 2, 3]': 3, '[3, 4, 1, 2, 3]': 3, '[1, 5, 3, 2, 4]': 4, '[1, 3, 1, 3, 2]': 3, '[1, 3, 2, 4, 2]': 3, '[4, 5, 3, 2, 1]': 4, '[1, 2, 5, 3, 4]': 4, '[2, 5, 4, 1, 3]': 4, '[2, 1, 4, 3, 1]': 3, '[3, 2, 5, 4, 1]': 4, '[3, 4, 1, 2, 4]': 3, '[3, 2, 1, 4, 2]': 3, '[1, 4, 3, 1, 2]': 3, '[2, 4, 1, 4, 3]': 3, '[4, 1, 4, 3, 2]': 3, '[4, 2, 1, 3, 5]': 4, '[1, 3, 1, 2, 4]': 3, '[3, 4, 3, 2, 1]': 3, '[2, 1, 3, 5, 4]': 4, '[2, 3, 2, 3, 1]': 3, '[1, 5, 4, 2, 3]': 4, '[4, 3, 5, 1, 2]': 4, '[1, 2, 4, 2, 3]': 3, '[4, 2, 3, 4, 1]': 3, '[3, 1, 5, 2, 4]': 4, '[2, 3, 1, 2, 1]': 3, '[5, 4, 1, 3, 2]': 4, '[3, 2, 4, 1, 4]': 3, '[3, 5, 4, 1, 2]': 4, '[5, 4, 2, 3, 1]': 4, '[4, 1, 2, 3, 1]': 3, '[1, 2, 3, 4, 1]': 3, '[3, 4, 2, 1, 2]': 3, '[2, 3, 1, 3, 4]': 3, '[4, 3, 5, 2, 1]': 4, '[1, 2, 4, 3, 2]': 3, '[5, 2, 3, 1, 4]': 4, '[4, 2, 5, 3, 1]': 4, '[3, 1, 4, 5, 2]': 4, '[3, 2, 4, 3, 1]': 3, '[4, 3, 4, 1, 2]': 3, '[2, 4, 2, 1, 3]': 3, '[5, 3, 2, 1, 4]': 4, '[1, 3, 2, 4, 1]': 3, '[4, 3, 1, 5, 2]': 4, '[2, 3, 4, 3, 1]': 3, '[1, 3, 2, 5, 4]': 4, '[5, 1, 4, 2, 3]': 4, '[3, 4, 1, 2, 1]': 3, '[4, 2, 1, 3, 2]': 3, '[4, 1, 2, 5, 3]': 4, '[1, 3, 4, 2, 3]': 3, '[3, 2, 1, 3, 4]': 3, '[3, 4, 2, 4, 1]': 3, '[1, 4, 3, 2, 1]': 3, '[1, 2, 3, 2, 4]': 3, '[2, 3, 4, 5, 1]': 4, '[4, 2, 1, 3, 1]': 3, '[2, 3, 1, 3, 2]': 3, '[2, 1, 3, 4, 1]': 3, '[3, 2, 3, 1, 2]': 3, '[4, 2, 1, 4, 3]': 3, '[2, 3, 1, 4, 1]': 3, '[4, 3, 1, 2, 3]': 3, '[2, 1, 3, 2, 3]': 3, '[3, 2, 4, 1, 3]': 3, '[5, 2, 1, 3, 4]': 4, '[2, 5, 4, 3, 1]': 4, '[2, 4, 2, 3, 1]': 3, '[1, 2, 3, 1, 2]': 3, '[4, 1, 3, 2, 1]': 3, '[2, 3, 1, 4, 2]': 3, '[1, 3, 1, 2, 1]': 2, '[3, 1, 2, 3, 2]': 3, '[2, 1, 3, 4, 2]': 3, '[2, 4, 5, 3, 1]': 4, '[1, 3, 1, 2, 3]': 3, '[2, 1, 4, 3, 4]': 3, '[1, 3, 5, 4, 2]': 4, '[4, 2, 3, 2, 1]': 3, '[3, 4, 1, 4, 2]': 3, '[2, 1, 3, 1, 2]': 3, '[3, 1, 3, 2, 1]': 3, '[1, 4, 2, 4, 3]': 3, '[3, 2, 3, 2, 1]': 3, '[5, 3, 2, 4, 1]': 4, '[4, 3, 1, 2, 5]': 4, '[4, 2, 1, 5, 3]': 4, '[1, 3, 4, 3, 2]': 3, '[1, 2, 3, 4, 2]': 3, '[2, 1, 3, 2, 1]': 3, '[2, 1, 2, 3, 1]': 3, '[1, 2, 4, 3, 1]': 3, '[1, 2, 4, 5, 3]': 4, '[3, 1, 2, 4, 2]': 3, '[3, 4, 1, 3, 2]': 3, '[2, 4, 1, 5, 3]': 4, '[1, 2, 4, 3, 4]': 3, '[5, 1, 4, 3, 2]': 4, '[3, 1, 2, 3, 1]': 3, '[2, 1, 3, 1, 3]': 3, '[1, 3, 4, 2, 1]': 3, '[2, 4, 3, 1, 3]': 3, '[3, 5, 1, 4, 2]': 4, '[3, 4, 3, 1, 2]': 3, '[3, 1, 3, 1, 2]': 3, '[1, 4, 3, 4, 2]': 3, '[5, 3, 4, 2, 1]': 4, '[1, 4, 1, 3, 2]': 3, '[1, 5, 4, 3, 2]': 4, '[4, 3, 2, 1, 4]': 3, '[1, 4, 3, 2, 5]': 4, '[4, 3, 2, 1, 2]': 3, '[3, 1, 4, 2, 1]': 3, '[2, 4, 1, 2, 3]': 3, '[1, 4, 3, 2, 3]': 3, '[1, 3, 4, 1, 2]': 3, '[2, 3, 2, 1, 3]': 3, '[2, 1, 4, 1, 3]': 3, '[3, 2, 3, 1, 3]': 2, '[4, 3, 1, 2, 1]': 3, '[2, 3, 1, 2, 4]': 3, '[1, 2, 1, 2, 3]': 3, '[3, 2, 1, 3, 1]': 3, '[3, 2, 1, 4, 1]': 3, '[1, 2, 3, 2, 3]': 3, '[1, 2, 1, 3, 1]': 2, '[4, 3, 2, 4, 1]': 3, '[1, 4, 1, 2, 3]': 3, '[3, 4, 2, 3, 1]': 3, '[4, 1, 3, 4, 2]': 3, '[4, 1, 2, 1, 3]': 3, '[4, 1, 2, 3, 2]': 3, '[3, 1, 2, 1, 2]': 3, '[3, 2, 3, 4, 1]': 3}
# dp = {}

dp_len = len(dp)

def press(arr):
  last = -1
  for i in range(len(arr)-1, -1, -1):
    if -1 != last and last == arr[i]:
      arr.pop(i)
    last = arr[i]
  tmp = [ 0 for _ in range(21) ]
  for n in arr:
    tmp[n] += 1
  
  cache = []
  cnt = 0
  for i in range(len(tmp)):
    if 0 < tmp[i]:
      cnt += 1
      cache.append(i)
  
  for i in range(len(arr)):
    arr[i] = cache.index(arr[i]) + 1
#TDD
u = [1,3,5]
press(u)
if u != [1,2,3]: print("ERR1", u)
u = [1,1,1,1,3,3,3,3,3,3,5,5,5,5,5]
press(u)
if u != [1,2,3]: print("ERR2", u)
u = [1,2,3,3,2,2,1]
press(u)
if u != [1,2,3,2,1]: print("ERR3", u)


# print(arr)
def visit(a, leftClosed, idx):
  l = len(a)
  if l == 0: return 0
  if l == 1: return 0
  if l == 2:
    if a[0] == a[1]: return 0
    return 1
  if l-1 <= idx: return l-1
  key = str(a)
  press(a)
  if not dbg:
    if key in dp:
      return dp[key]

  a1 = list(a)

  c1 = visit(a1, False, idx+1)
  c3 = c2 = c1
  if not leftClosed:
    v = 1
    if a[idx] == a[idx-1]: v = 0
    a2 = list(a)
    a2.pop(idx)
    press(a2)
    c2 = visit(a2, False, idx) + v # merge to left
  if idx < l-1:
    v = 1
    if a[idx] == a[idx+1]: v = 0
    a3 = list(a)
    a3.pop(idx)
    press(a3)
    c3 = visit(a3, True,  idx) + v # merge to right

  m = min(c1,min(c2,c3))
  if not key in dp:
    dp[key] =     m
    if dbg: print("key=> ", key, " val=",dp[key])
  else:
    if m != dp[key]:
      if dbg: print("key-> ", key, " val=",dp[key])
    m = min(m, dp[key])
    dp[key] = m
  return m

rp = 1
if dbg: rp = 10000
for z in range(rp):
  N,K = map(int, f().split())
  if dbg:
    N = random.randint(1,5)
    K = random.randint(1,20)

  arr = list(map(int, f().split()))
  if dbg:
    arr = [ random.randint(1,K) for _ in range(N) ]

  press(arr)

  # TO GO
  ans = visit(arr, True, 0)
  ## print(ans)


print(ans)
if dbg:
  print(dp)
  print('ori', dp_len)
  print('new', len(dp))

# TDD
test = [1]
k = visit(test, True, 0)
if k != 0: print("[ERR-1]", k)
test = [1,1]
k = visit(test, True, 0)
if k != 0: print("[ERR-2]", k)
test = [1,2]
k = visit(test, True, 0)
if k != 1: print("[ERR-3]", k)
test = [1,2,3]
k = visit(test, True, 0)
if k != 2: print("[ERR-4]", k)
test = [1,2,1]
k = visit(test, True, 0)
if k != 1: print("[ERR-5]", k)
test = [1,2,2,2,2,1]
k = visit(test, True, 0)
if k != 1: print("[ERR-6]", k)
test = [1,2,3,3,2,2,1]
k = visit(test, True, 0)
if k != 2: print("[ERR-7]", k)
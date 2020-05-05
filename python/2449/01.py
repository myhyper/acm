# 기본 입력을 받는다.
import sys
f = sys.stdin.readline
dbg = 1
if dbg: f = open('input1.txt').readline
N,K = map(int, f().split())
arr = list(map(int, f().split()))

# test
print(arr)
# 해당문제 강의 https://www.youtube.com/watch?v=xOlhR_2QCXY
# DP 강의 1 http://bopace.github.io/python/2016/04/27/python-and-dp/
# DP 강의 2 https://skerritt.blog/dynamic-programming/


# recursive solution

# def KS(n, c):
#     if n == 0 or c == 0:
#         result = 0
#     elif w[n] > c:
#         result = KS(n-1, c)
#     else:
#         temp1 = KS(n-1, c)
#         temp2 = v[n] + KS(n-1, c-w[n])
#         result = max(temp1, temp2)
#     return result
#
#
# N, C = map(int, input().split())
# w = [0]
# v = [0]
# for _ in range(N):
#     a, b = map(int, input().split())
#     w.append(a)
#     v.append(b)
# print(w)
# print(v)
# print(KS(N, C))

# memorize intermediate results

def KS(n, c):
    if arr[n][c] != 'undefined': return arr[n][c]
    if n == 0 or c == 0:
        result = 0
    elif w[n] > c:
        result = KS(n-1, c)
    else:
        temp1 = KS(n-1, c)
        temp2 = v[n] + KS(n-1, c-w[n])
        result = max(temp1, temp2)
    arr[n][c] = result
    return result


N, C = map(int, input().split())
w = [0]
v = [0]
arr = [['undefined'] * (C+1) for _ in range(N+1)]

for _ in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
print(KS(N, C))

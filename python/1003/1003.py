debug = True
debug = None

if debug:
    f = open("input1003.txt")
    i = f.readline()
else:
    i = input()

t = int(i)
arr = [0] * 41
arr[1] = 1
for j in range(t):
    if debug:
        i = f.readline()
    else:
        i = input()
    n = int(i)
    if 0 == n:
        print("1 0")
        continue
    for k in range(2, n+1):
        arr[k] = arr[k-1] + arr[k-2]
    print("{} {}".format(arr[n-1],arr[n]))
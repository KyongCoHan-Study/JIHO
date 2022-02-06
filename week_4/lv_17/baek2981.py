import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(N)]

for j in range(2, max(arr)+1):
    temp = arr[0] % j
    for val in arr:
        if val % j != temp:
            temp = -1
            break
    if temp != -1:
        print(j, end=" ")

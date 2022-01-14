N = int(input())

arr = []
sol = [1 for i in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

for i in range(N):
    for j in range(N):
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            sol[i] += 1


ans = " ".join(map(str, sol))
print(ans)

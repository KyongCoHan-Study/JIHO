N = int(input())
pattern = ["***", "* *", "***"]
stars = []
for i in range(0, N, 3):
    for j in range(0, N, 3):
        stars.append(pattern)

for val in stars:
    print(val)
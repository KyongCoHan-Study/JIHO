N = int(input())

count = 1
num = 666
arr = [num]
a = num
while count < N:
    temp = a + 1
    if '666' in str(temp):
        if temp not in arr:
            arr.append(temp)
            count += 1
        else:
            a = temp
            continue
    else:
        a = temp

print(arr[-1])

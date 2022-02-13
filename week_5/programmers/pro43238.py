def check(v, times):
    sum = 0
    for t in times:
        sum += v // t
    return sum


def solution(n, times):
    answer = 0
    lt, rt = 1, max(times) * n
    while lt <= rt:
        mid = (lt + rt) // 2
        if check(mid, times) >= n:
            answer = mid
            rt = mid - 1
        else:
            lt = mid + 1

    return answer
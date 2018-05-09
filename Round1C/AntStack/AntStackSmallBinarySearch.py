# top down approach with binary search

def dp(i, j, mem):
    if j == 0:
        return 0

    if i == 0:
        return weights[0] if j == 1 else 2 ** 32

    if (i, j) in mem:
        return mem[(i, j)]

    res1 = dp(i - 1, j, mem)
    res2 = dp(i - 1, j - 1, mem)

    if res2 <= weights[i] * 6:
        res1 = min(res1, res2 + weights[i])

    mem[(i, j)] = res1
    return res1


def solve(weights):
    MAX_ANT = 139
    maxAns = min(MAX_ANT, len(weights))

    start, end = 1, maxAns
    mem = {}
    l = len(weights)

    while start + 1 < end:
        m = (start + end) // 2
        if dp(l - 1, m, mem) < 2 ** 32:
            start = m
        else:
            end = m - 1

    if dp(l - 1, start + 1, mem) < 2 ** 32:
        start += 1

    return start


t = int(input())
for i in range(1, t + 1):
    N = int(input())
    weights = [int(w) for w in input().split(' ')]
    ans = solve(weights)
    print("Case #{}: {}".format(i, ans))
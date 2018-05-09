# DP with bottom up

def solve(weights):
    MAX_ANT = 139
    maxAns = min(MAX_ANT, len(weights))

    mem = [[0 for _ in range(maxAns + 1)] for _ in range(len(weights))]

    for i in range(len(weights)):
        for j in range(maxAns + 1):
            if j == 0:
                mem[i][j] = 0
                continue

            if i == 0:
                mem[i][j] = weights[0] if j == 1 else 2 ** 32
                continue

            res1 = mem[i - 1][j]
            res2 = mem[i - 1][j - 1]
            if res2 <= weights[i] * 6:
                res1 = min(res1, res2 + weights[i])

            mem[i][j] = res1

    ans = 1
    for i in range(maxAns, 1, -1):
        if mem[len(weights) - 1][i] < 2 ** 32:
            ans = i
            break

    return ans


t = int(input())
for i in range(1, t + 1):
    N = int(input())
    weights = [int(w) for w in input().split(' ')]
    ans = solve(weights)
    print("Case #{}: {}".format(i, ans))
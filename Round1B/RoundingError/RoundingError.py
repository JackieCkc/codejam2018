import heapq
from math import ceil

def getNum(N, c):
    diff = (c / N * 100) % 1
    oneVoteDiff = (1 / N * 100) % 1
    diff = 1.5 - diff if diff >= 0.5 else 0.5 - diff
    return ceil(diff / oneVoteDiff)

def solve():
    t = int(input())

    for case in range(1, t + 1):
        N, L = [int(s) for s in input().split(" ")]
        votes = [int(s) for s in input().split(" ")]

        if (1 / N * 100) % 1 == 0:
            print("Case #{}: {}".format(case, 100))
            continue

        res = []

        for vote in votes:
            heapq.heappush(res, (getNum(N, vote), vote))

        remaining = N - sum(votes)
        a = getNum(N, 0)

        for _ in range(remaining):
            heapq.heappush(res, (a, 0))

        for _ in range(remaining):
            _, vote = heapq.heappop(res)
            heapq.heappush(res, (getNum(N, vote + 1), vote + 1))

        res = sum(int(numVotes / N * 100 + 0.5) for _, numVotes in res)
        print("Case #{}: {}".format(case, res))

solve()
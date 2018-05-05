import sys
from collections import Counter


def solve():
    t = int(input())

    for case in range(1, t + 1):
        N = int(input())

        remaining = set(range(N))
        occurrence = Counter()

        for i in range(N):
            favors = [int(s) for s in input().split(" ")]

            for favor in favors[i:]:
                occurrence[favor] += 1

            favors = sorted(favors[1:], key=lambda e: occurrence[e])

            for favor in favors:
                if favor not in remaining:
                    continue

                remaining.remove(favor)
                print(favor)
                break

            else:
                print(-1)

            sys.stdout.flush()


solve()

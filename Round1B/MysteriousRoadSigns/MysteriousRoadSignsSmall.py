# Brute force solution on test set 1, O(n ^ 3)

def solve():
    t = int(input())

    for case in range(1, t + 1):
        S = int(input())

        signs = []
        for _ in range(S):
            D, A, B = input().split(" ")
            signs.append((int(D) + int(A), int(D) - int(B)))

        maxLength, count = 0, 0

        ans = set()

        for i in range(S):
            sign = signs[i]

            for k in range(2):
                M = sign[k]
                N = None

                for j in range(i + 1, S):
                    Mj, Nj = signs[j]
                    if k == 1:
                        Mj, Nj = Nj, Mj

                    if N is not None and Nj == N:
                        continue

                    if Mj != M:
                        if N is None:
                            N = Nj
                        elif Nj != N:
                            if j - i > maxLength:
                                maxLength = j - i
                                count = 1
                                ans = {(i, j)}
                            elif j - i == maxLength and (i, j) not in ans:
                                count += 1
                                ans.add((i, j))

                            break
                else:
                    if S - i > maxLength:
                        maxLength = S - i
                        count = 1
                        ans = {(i, S)}
                    elif S - i == maxLength and (i, S) not in ans:
                        count += 1
                        ans.add((i, S))

        print("Case #{}: {} {}".format(case, maxLength, count))

solve()
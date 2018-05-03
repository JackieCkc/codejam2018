# Solution on test set 2, O(n log n)

def getCandidate(arr, t, useM):
    for mj, nj in arr:
        t1 = mj if useM else nj
        if t1 == t:
            continue

        return nj if useM else mj

    return None


def getCandidates(signs, i, useM):
    m, n = signs[i]
    t = m if useM else n
    c1 = getCandidate(signs[i + 1:], t, useM)
    c2 = getCandidate(signs[0:i][::-1], t, useM)
    return [c1, c2]


def getLength(arr, m, n):
    length = 0

    for mj, nj in arr:
        if mj != m and nj != n:
            break

        length += 1

    return length


def tryCandidates(arr, i, m, n):
    length1 = getLength(arr[:i][::-1], m, n)
    length2 = getLength(arr[i+1:], m, n)
    return [1 + length1 + length2, (i - length1, i + length2)]


def getMaxLength(signs):
    if len(signs) == 0:
        return [0, 0]

    if len(signs) <= 2:
        return [len(signs), 1]

    middleIndex = len(signs) // 2
    m, n = signs[middleIndex]
    n1, n2 = getCandidates(signs, middleIndex, True)
    m1, m2 = getCandidates(signs, middleIndex, False)
    candidates = [(m, n1), (m, n2), (m1, n), (m2, n)]

    maxLength = 0
    ranges = set()

    for mCandidate, nCandidate in candidates:
        currLength, currRange = tryCandidates(signs, middleIndex, mCandidate, nCandidate)

        if currLength > maxLength:
            ranges = {currRange}
            maxLength = currLength
        elif currLength == maxLength:
            ranges.add(currRange)

    count = len(ranges)

    maxLengthLeft, countLeft = getMaxLength(signs[:middleIndex])
    maxLengthRight, countRight = getMaxLength(signs[middleIndex+1:])

    allMax = max(maxLength, maxLengthLeft, maxLengthRight)

    allCount = 0
    if maxLength == allMax:
        allCount += count
    if maxLengthLeft == allMax:
        allCount += countLeft
    if maxLengthRight == allMax:
        allCount += countRight

    return [allMax, allCount]


def solve():
    t = int(input())

    for case in range(1, t + 1):
        S = int(input())

        signs = []
        for _ in range(S):
            D, A, B = input().split(" ")
            signs.append((int(D) + int(A), int(D) - int(B)))

        maxLength, count = getMaxLength(signs)
        print("Case #{}: {} {}".format(case, maxLength, count))

solve()
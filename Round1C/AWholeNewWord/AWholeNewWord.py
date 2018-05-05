class Solution:
    newWord = None

    def dfs(self, curr, L, words, arr):
        if self.newWord is not None:
            return

        if len(curr) == L:
            if curr not in words:
                self.newWord = curr
            return

        for c in arr[len(curr)]:
            self.dfs(curr + c, L, words, arr)

    def solve(self):
        t = int(input())

        for case in range(1, t + 1):
            N, L = [int(s) for s in input().split(" ")]

            words = set()
            for _ in range(N):
                words.add(input())

            arr = [set() for _ in range(L)]

            for word in words:
                for i, c in enumerate(word):
                    arr[i].add(c)

            combinations = 1
            for s in arr:
                combinations *= len(s)

            if N >= combinations:
                print("Case #{}: {}".format(case, '-'))
                continue

            self.newWord = None
            self.dfs('', L, words, arr)

            print("Case #{}: {}".format(case, self.newWord))


Solution().solve()

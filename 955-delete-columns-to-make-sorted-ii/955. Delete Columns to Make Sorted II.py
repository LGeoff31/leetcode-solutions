class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        resolved = [False] * (n - 1)
        unresolved = n - 1
        deletions = 0

        for col in range(m):
            if unresolved == 0:
                break

            bad = False
            for i in range(n - 1):
                if not resolved[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            if bad:
                deletions += 1
                continue

            for i in range(n - 1):
                if not resolved[i] and strs[i][col] < strs[i + 1][col]:
                    resolved[i] = True
                    unresolved -= 1

        return deletions
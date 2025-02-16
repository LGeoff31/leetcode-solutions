from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def backtrack(idx: int) -> bool:
            if idx == len(res):
                return True  # Valid sequence found
            
            if res[idx] != 0:  # Skip already filled positions
                return backtrack(idx + 1)

            for i in range(n, 0, -1):  # Try placing from largest to smallest
                if used[i]:
                    continue
                if i == 1:  # '1' only appears once
                    res[idx] = 1
                    used[i] = True
                    if backtrack(idx + 1):
                        return True
                    res[idx] = 0
                    used[i] = False
                else:
                    if idx + i < len(res) and res[idx + i] == 0:  # Can place both occurrences
                        res[idx] = res[idx + i] = i
                        used[i] = True
                        if backtrack(idx + 1):
                            return True
                        res[idx] = res[idx + i] = 0
                        used[i] = False

            return False

        backtrack(0)
        return res

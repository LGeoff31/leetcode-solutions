class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        @cache
        def dfs(index):
            if index == n - 1:
                return [index + 1], 0
            best, best_val = [], 1e9
            for j in range(index+1, index+maxJump+1):
                if j >= len(coins): break
                if coins[j] == -1:
                    continue
                A, val = dfs(j)
                val += coins[j]
                if val < best_val:
                    best, best_val = A, val
            return [index + 1] + best, best_val
        arr, val = dfs(0)
        if val < 1e8:
            return arr
        print(val)
        return []
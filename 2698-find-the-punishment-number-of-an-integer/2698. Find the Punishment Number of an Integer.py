class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        def dfs(expr, target, idx, n):
            if idx == n and target == 0:
                return True
            elif target < 0: 
                return False
            curr = 0
            for i in range(idx, n):
                curr = curr * 10 + int(expr[i])
                if dfs(expr, target - curr, i+1, n):
                    return True
            return False

        for i in range(1, n+1):
            if dfs(str(i*i), i, 0, len(str(i*i))):
                res += i * i
        return res
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        size = len(s)
        res = 0

        def fac(n): 
            if n == 0: 
                return 0 
            cnt = 1 
            b = 10 
            while n > 0: 
                if cnt == 1:
                    cnt *= 9
                    b -= 1
                    n -= 1
                    continue
                cnt *= b 
                b -= 1 
                n -= 1 
            return cnt 

        for i in range(1, len(str(n))): 
            res += fac(i)

        def dfs(i, tight, mask):
            if i == size:
                return 1

            limit = int(s[i]) if tight else 9
            ans = 0

            for digit in range(0, limit + 1):
                if i == 0 and digit == 0:
                    continue

                if mask & (1 << digit):
                    continue

                new_tight = tight and digit == limit
                ans += dfs(i + 1, new_tight, mask | (1 << digit))

            return ans

        res += dfs(0, True, 0)
        return res
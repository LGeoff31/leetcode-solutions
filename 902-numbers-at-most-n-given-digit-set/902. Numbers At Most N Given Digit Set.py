class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        res = 0
        n_len = len(str(n))
        n_str = str(n)
        for i in range(1, n_len):
            res += len(digits) ** i
        @cache
        def dfs(i, isLimited): # Indicies will be at most logn
            if i == n_len:
                return 1
            cnt = 0
            upper_limit = n_str[i] if isLimited else '9'
            for digit in digits:
                if digit > upper_limit:
                    break
                cnt += dfs(i+1, isLimited and digit == n_str[i])
            return cnt
        res += dfs(0, True)
        return res
                
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        """
        [5,2,-8, 1]
        """
        if sum(balance) < 0:
            return -1
        min_val = min(balance)
        if min_val >= 0:
            return 0

        # ITS POSSIBLE TO TRANSFER TO IT
        # GREEDY: try neighbors transfer everything first
        n = len(balance)
        reversed = False
        l, r = balance.index(min(balance)) - 1, balance.index(min(balance)) + 1 
        if r >= n: 
            reversed = True
            r %= n
        if l < 0:
            reversed = True
            l %= n
        cnt = 1
        res = 0
        print(l, r)
        while (l <= r and not reversed) or (l >= r and reversed):
            if balance[l] >= abs(min_val):
                res += min(cnt, n-cnt) * abs(min_val)
                return res
            else:
                min_val += balance[l]
                res += balance[l] * min(cnt, n-cnt)
                l -= 1
                if l < 0: reversed = True
                l %= n

            if balance[r] >= abs(min_val):
                res += min(cnt, n-cnt) * abs(min_val)
                return res
            else:
                min_val += balance[r]
                res += balance[r] * min(cnt, n-cnt)
                r += 1
                if r >= n: reversed=True
                r %= n

            # res += cnt
            cnt += 1
            print(l, r, cnt, res)

        return res
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        """
        -1 if 

        poowers of 5
        1 = 5^0
        101 = 5^1
        1101 = 5^2
        1111101 = 5^3
        1001110001 = 5^4

        BIG QUEESTION
        Is there a case where we might want to extend the string despite the current substring being power 5?

        """
        def power_five(string):
            if not string or string[0] == "0":
                return False
            val = int(string, 2)
            if val == 0: return False
            while val > 1:
                if val % 5 != 0:
                    return False
                val //= 5
            return True
        ans = 1e9
        @cache
        def dfs(curr, i, tally):
            nonlocal ans
            if i == len(s):
                if curr and power_five(curr):
                    ans = min(ans, tally+1)
                return
            # TAKE
            dfs(curr+s[i], i+1, tally)
            # DONT TAKE
            if curr and power_five(curr):
                dfs(s[i], i+1, tally + 1)

        dfs("", 0, 0)
        return ans if ans != 1e9 else -1
        
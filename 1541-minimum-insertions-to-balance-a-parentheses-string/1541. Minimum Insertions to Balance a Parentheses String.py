class Solution:
    def minInsertions(self, s: str) -> int:
        open = ans = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open += 1
            else:
                # Step 1: make a "))"
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1

                # Step 2: find its '('
                if open > 0:
                    open -= 1
                else:
                    ans += 1
            i += 1

        return ans + open * 2
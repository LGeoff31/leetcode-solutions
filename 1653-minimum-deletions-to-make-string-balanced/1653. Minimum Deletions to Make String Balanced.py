class Solution:
    def minimumDeletions(self, s: str) -> int:
        if "a" not in s or "b" not in s:
            return 0
        lst = [[0, 0] for _ in range(len(s))]

        if s[0] == "a":
            lst[0][0] = 1
        else:
            lst[0][1] = 1

        for i in range(1, len(s)):
            if s[i] == "a":
                lst[i][1] = lst[i-1][1]
                lst[i][0] = 1 + lst[i-1][0]
            else:
                lst[i][1] = 1 + lst[i-1][1]
                lst[i][0] = lst[i-1][0]

        res = 1e9
        total_a, total_b = s.count("a"), s.count("b")
        for i in range(len(lst)):
            a_before, b_before = lst[i]
            a_after = total_a - a_before
            res = min(res, b_before + a_after)
            
        return min(res, s.count("a"), s.count("b"))

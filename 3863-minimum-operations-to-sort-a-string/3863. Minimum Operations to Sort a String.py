class Solution:
    def minOperations(self, s: str) -> int:
        if all(map(le, s, s[1:])):  # already sorted
            return 0
        if len(s) == 2:  # only single letters can be sorted, which changes nothing
            return -1

        mid = lambda: islice(s, 1, len(s) - 1)  # the middle, without copying it
        lo, hi = min(mid()), max(mid())
        if s[0] <= min(lo, s[-1]) or max(s[0], hi) <= s[-1]:  # the first letter is the smallest, or the last the largest
            return 1
        return 3 if s[-1] < lo <= hi < s[0] else 2  # the middle sits strictly between the last letter and the first
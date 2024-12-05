class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        c = 0
        weight.sort()
        curr = 0
        for w in weight:
            curr += w
            if curr <= 5000:
                c += 1
            else:
                break
        return c
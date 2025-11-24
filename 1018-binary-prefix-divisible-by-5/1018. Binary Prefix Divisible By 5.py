class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        curr = ""
        for n in nums:
            curr += str(n)
            val = int(curr, 2)

            res.append(val % 5 == 0)
        return res

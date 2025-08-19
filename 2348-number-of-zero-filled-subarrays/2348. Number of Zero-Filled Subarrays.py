class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for n in nums:
            if n == 0:
                curr += 1
            else:
                res += curr * (curr + 1) // 2
                curr = 0
        if curr:
            res += curr * (curr + 1) // 2
        return res
class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        """
        Go 1 -> N O(n)
            Loop to cap every element O(n)
            Use DP to determine predicate O(n)
        
        Sort the nums, then it's more evident which elements will be changed and which won't

        """

        res = []
        n = len(nums)
        T = (1 << (k+1)) - 1
        for i in range(1, n+1):
            curr = 1
            for n in nums:
                curr |= curr << min(n, i)
                if (curr & (1 << k) > 0):
                    break
                curr &= T
            res.append(curr & (1 << k) > 0)

        return res

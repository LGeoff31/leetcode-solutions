class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        """
        do we remove min elemtn or max elemnt???
        [1,2,6,9], k=3
        """
        res = 1e9
        n = len(nums)
        r = 0
        for l in range(len(nums)):
            while r < len(nums) and nums[l] * k >= nums[r]:
                r += 1
            
            res = min(res, n-(r-l))
            l += 1

        return res
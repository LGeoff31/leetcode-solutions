class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-1):
            leftSubarr = nums[:i+1]
            rightSubarr = nums[i+1 : ]
            if (sum(leftSubarr) - sum(rightSubarr)) % 2 == 0:
                res += 1
        return res
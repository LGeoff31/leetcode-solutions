class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n-1):
            # partition at i
            leftArr = nums[:i]
            rightArr = nums[i:]
            if abs(sum(leftArr) - sum(rightArr))%2==0:
                res += 1
        return res
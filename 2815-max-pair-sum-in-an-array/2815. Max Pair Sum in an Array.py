class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def maxDigit(num):
            a = []
            for b in str(num):
                a.append(int(b))
            return max(a)
        res = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] > res and maxDigit(nums[i]) == maxDigit(nums[j]):
                    res = nums[i] + nums[j]
        return res        
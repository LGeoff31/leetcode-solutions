class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        """
        subsequence of size m, maximize product first and last element on subsequence
        to maximize product, can either be two negatives multiply or two positives
        Observation: You ultimately want to pick the two numbers, how will we guarantee subsequence will be size m
        If the two numbers at at indicies (i, j), i < j, if j-i+1 >= m, it is valid

        positive[i] gives most positive value from i -> end,
        negative[i] gives most negative value from i -> end

        loop through nums, go up by jump m-1, max(nums[i] * positive[i], nums[i] * negative[i])

        EDGE CASE 1 ELEMENT
        """
        if len(nums) == 1:
            if m == 1:
                return nums[0] * nums[0]
            return 0
        positive = [-1e9] * len(nums)
        negative = [1e9] * len(nums)
        curr = -1e9
        for i in range(len(nums) -1, -1, -1):
            curr = max(curr, nums[i])
            positive[i] = curr
        curr = 1e9
        for i in range(len(nums) - 1, -1, -1):
            curr = min(curr, nums[i])
            negative[i] = curr
        res = -1e20
        
        for i in range(len(nums)):
            if i+m-1 < len(positive):
                res = max(res, nums[i] * positive[i+m-1], nums[i] * negative[i+m-1])
        print(res)
        return res

        return 0
            
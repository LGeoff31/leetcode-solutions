class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        def product_array(nums):
            total = 1
            for char in nums:
                total *= char
            return total

        for i in range(len(nums)):  # O(N)
            a = nums[:i] + nums[i+1:]  # O(N)
            res.append(product_array(a))

        return res

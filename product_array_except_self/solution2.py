class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        postfix = []
        total_prefix = 1
        total_postfix = 1
        for num in nums:
            total_prefix *= num
            prefix.append(total_prefix)
        for i in reversed(range(len(nums))):
            total_postfix *= nums[i]
            postfix.append(total_postfix)
        postfix = postfix[::-1]

        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i+1])
            elif i == len(nums) - 1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1] * postfix[i+1])

        return res

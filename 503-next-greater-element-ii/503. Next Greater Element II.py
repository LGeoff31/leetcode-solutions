class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums
        res = []

        for i in range(n):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]: 
                    res.append(nums[j])
                    break
            else:
                res.append(-1)
        return res
            
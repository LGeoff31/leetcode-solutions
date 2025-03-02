class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        if k == 1: 
            a = -1
            dic = Counter(nums)
            for key in dic:
                if dic[key] == 1:
                    a = max(a, key)
            return a
        a = b = -1
        if nums.count(nums[0]) == 1:
            a = nums[0]
        if nums.count(nums[-1]) == 1:
            b = nums[-1]
        return max(a,b)
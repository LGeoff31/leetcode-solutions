class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = set(nums)
        for num in a:
            if nums.count(num) > len(nums)//2:
                return num
        
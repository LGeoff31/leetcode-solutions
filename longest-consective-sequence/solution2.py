class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        a = set(nums)
        nums = list(a)
        nums.sort()
        max_length = 1
        length = 1
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                length += 1
                if i == len(nums)-2:
                    max_length = max(max_length, length)
            else:
                max_length = max(max_length, length)
                length = 1
        return max_length

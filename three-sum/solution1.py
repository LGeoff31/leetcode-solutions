class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # [-4, -1, -1, 0, 1, 2]
        for i, value in enumerate(nums):
            if i > 0 and value == nums[i-1]:
                continue
            left, right = i+1, len(nums) - 1  # 1, 4
            while left < right:
                threeSum = value + nums[left] + nums[right]
                if threeSum == 0:
                    res.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    left += 1
        return res

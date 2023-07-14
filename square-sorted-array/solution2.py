class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        length = len(nums)
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                nums.append(nums[left] * nums[left])
                left += 1
            else:
                nums.append(nums[right] * nums[right])
                right -= 1
        result = nums[length:]
        return result[::-1]

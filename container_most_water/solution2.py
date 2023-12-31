class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height) - 1
        curr_water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, curr_water)
        while left < right:
            if height[right] < height[left]:
                right -= 1
                curr_water = min(height[left], height[right]) * (right - left)
                max_water = max(max_water, curr_water)
            else:
                left += 1
                curr_water = min(height[left], height[right]) * (right - left)
                max_water = max(max_water, curr_water)
        return max_water

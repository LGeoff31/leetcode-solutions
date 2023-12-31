class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                width = j - i
                possible_height = min(height[i], height[j])
                max_water = max(max_water, width * possible_height)
        return max_water

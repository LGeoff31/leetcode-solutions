class Solution:
    def maxArea(self, height: List[int]) -> int:
        """ 
        height = [1,8,6,2,5,4,8,3,7]
                        ^ ^         

        Time complexity: O(n)
        Space complexity: O(1)

        """
        global_maximum_area = 0
        l, r = 0, len(height) - 1
        while l <= r:
            global_maximum_area = max(global_maximum_area, (r-l) * min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return global_maximum_area


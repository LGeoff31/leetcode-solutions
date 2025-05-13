class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (idx, height)
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                res = max(res, (i-idx) * height)
                start = idx
            
            stack.append((start, h))
            res = max(res, (i - stack[-1][0]) * stack[0][0])
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res
            

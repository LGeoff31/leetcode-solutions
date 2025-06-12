class Solution:
    def trap(self, height: List[int]) -> int:   
        left, right = [-1e9], [-1e9]
        n = len(height)
        curr = -1e9
        for i in range(n):
            curr = max(curr, height[i])
            left.append(curr)
        curr = -1e9
        for i in range(n-1, -1, -1):
            curr = max(curr, height[i])
            right.append(curr)
        res = 0
        right = right[::-1]
        print(left)
        print(right)
        for i in range(n):
            res += max(min(left[i], right[i]) - height[i],0)
            print(res)
        return res
        


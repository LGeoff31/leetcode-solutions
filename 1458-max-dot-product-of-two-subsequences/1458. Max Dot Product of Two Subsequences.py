class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return 0            
            return max(dfs(i+1, j), dfs(i, j+1), nums1[i]*nums2[j] + dfs(i+1, j+1))
        
        ans = dfs(0, 0)
        if ans == 0:
            if 0 in nums1 or 0 in nums2:
                return 0
            return max(max(nums1) * min(nums2), max(nums2) * min(nums1))
        return ans
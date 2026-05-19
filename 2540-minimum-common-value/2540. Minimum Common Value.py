class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        res = float('inf')
        nums2 = set(nums2)
        for n in nums1:
            if n in nums2:
                res = min(res, n)
        return res if res != float('inf') else -1
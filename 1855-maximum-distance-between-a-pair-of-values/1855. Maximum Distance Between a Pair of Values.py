class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        a,b = 0, 0
        res = 0
        while a < len(nums1) and b < len(nums2):
            while b < len(nums2) and nums1[a] <= nums2[b]:
                res = max(res, b-a)
                b += 1

            a += 1
        return res
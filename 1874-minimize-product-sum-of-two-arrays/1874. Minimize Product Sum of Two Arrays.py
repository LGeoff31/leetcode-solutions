class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        res = 0
        for i in range(len(nums1)):
            res += nums1[i] * nums2[i]
        return res
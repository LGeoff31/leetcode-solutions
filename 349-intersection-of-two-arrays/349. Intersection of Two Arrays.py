class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set()
        for num in nums1:
            if num in nums2:
                a.add(num)
        return list(a)
        
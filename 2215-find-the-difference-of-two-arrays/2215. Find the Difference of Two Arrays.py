class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        a,b = set(nums1), set(nums2)
        c = set()
        d = set()
        for num in nums1:
            if num not in b and num not in c:
                c.add(num)
        res.append(list(c))
        for num in nums2:
            if num not in a and num not in d:
                d.add(num)
        res.append(list(d))
        return res

        
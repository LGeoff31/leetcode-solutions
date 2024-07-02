class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        a,b = Counter(nums1), Counter(nums2)
        for key in a:
            if key in b:
                for i in range(min(a[key], b[key])):
                    res.append(key)
        return res

        
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            idx = nums2.index(num)
            for i in range(idx+1, len(nums2)):
                if nums2[i] > num:
                    res.append(nums2[i])
                    break
            else:
                res.append(-1)
        return res
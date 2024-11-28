class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Idea: each num1 will appear m times and each num2 will appear n times
        # Hence we only care if m and n are odd
        n, m = len(nums1), len(nums2)
        freq = {}
        for i in range(len(nums1)):
            freq[nums1[i]] = m + freq.get(nums1[i], 0)
        for i in range(len(nums2)):
            freq[nums2[i]] = n + freq.get(nums2[i], 0)
        res = 0
        for key in freq:
            if freq[key] % 2:
                res ^= key
        return res
        
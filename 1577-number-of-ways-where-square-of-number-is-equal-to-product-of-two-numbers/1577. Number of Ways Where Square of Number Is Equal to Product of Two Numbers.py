class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        #type 1
        dic1 = {}
        for i in range(len(nums1)):
            dic1[nums1[i] ** 2] = 1 + dic1.get(nums1[i] ** 2, 0)
        

        set1 = set(list(n**2 for n in nums1))
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                if nums2[i] * nums2[j] in dic1:
                    res += dic1[nums2[i] * nums2[j]]
        print(res)
        #type 2
        dic2 = {}
        for i in range(len(nums2)):
            dic2[nums2[i] ** 2] = 1 + dic2.get(nums2[i] ** 2, 0)

        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                if nums1[i] * nums1[j] in dic2:
                    res += dic2[nums1[i] * nums1[j]]
        return res
        
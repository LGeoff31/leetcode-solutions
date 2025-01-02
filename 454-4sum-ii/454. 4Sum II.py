class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        n = len(nums1)
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        for i in range(n):
            for j in range(n):
                dic1[nums1[i] + nums2[j]] += 1
        for i in range(n):
            for j in range(n):
                dic2[nums3[i] + nums4[j]] += 1
        print(dic1)
        print(dic2)
        for pair_sum in dic1:
            if -pair_sum in dic2:
                res += dic2[-pair_sum] * dic1[pair_sum]
        return res

        # dic = {}
        # nums4_dic = Counter(nums4)
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             if -(nums1[i] + nums2[j] + nums3[k]) in nums4_dic:
        #                 res += nums4_dic[-(nums1[i] + nums2[j] + nums3[k])]
        # return res
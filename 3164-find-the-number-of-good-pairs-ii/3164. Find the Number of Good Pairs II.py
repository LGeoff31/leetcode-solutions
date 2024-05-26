factors = [[] for _ in range(10 ** 6 + 1)]
for i in range(1, 10 ** 6 + 1):
    for j in range(i, 10 ** 6 + 1, i):
        factors[j].append(i)
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1 = [num // k for num in nums1 if num % k == 0]
        nums2 = Counter(nums2)
        res = 0 
        for num in nums1:
            for factor in factors[num]:
                if factor in nums2:
                    res += nums2[factor]
        return res
        


        
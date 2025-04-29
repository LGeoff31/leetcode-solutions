class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        res = 0
        dic = defaultdict(int)
        for i in range(len(nums)):
            for j in range(len(nums)):
                dic[nums[i] & nums[j]] += 1
        
        for num in nums:
            for k, v in dic.items():
                if num & k == 0:
                    res += v
        
        return res
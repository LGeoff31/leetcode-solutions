class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int) # Prefix Sum : Frequency
        dic[0] = 1
        accumulate = 0
        res = 0
        for i, num in enumerate(nums):
            accumulate += num

            target_value = accumulate - k
            if target_value in dic:
                res += dic[target_value]
                
            dic[accumulate] += 1

        return res
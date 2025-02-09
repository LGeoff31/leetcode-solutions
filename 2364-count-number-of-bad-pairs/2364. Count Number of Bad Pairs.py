class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        dic = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] - i in dic:
                res += dic[nums[i] - i]
            
            dic[nums[i] - i] += 1
        return n*(n-1)//2 - res
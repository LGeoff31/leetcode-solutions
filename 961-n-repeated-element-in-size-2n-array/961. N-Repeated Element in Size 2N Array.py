class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        dic = Counter(nums)
        for key in dic:
            if dic[key] == n:
                return key
class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        dic = defaultdict(int)
        res = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                dic[tuple(sorted([nums[i], nums[i-1]]))] += 1
            else:
                res += 1
        if not len(dic):
            return res
        return res + max(dic.values())
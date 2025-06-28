class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        a = sorted(nums)
        dic = defaultdict(int)
        for i in range(len(a) - 1, len(a) -1 - k, -1):
            dic[a[i]] += 1
        res = []
        for i in range(len(nums)):
            if nums[i] in dic:
                res.append(nums[i])
                dic[nums[i]] -= 1
                if dic[nums[i]] == 0:
                    del dic[nums[i]]
        return res
class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        res = []
        dic = defaultdict(int)
        # initialize
        for i in range(k):
            dic[nums[i]] += 1
        idx = i + 1
        res.append(len(dic))
        l = 0
        while idx < len(nums):
            dic[nums[l]] -= 1
            if dic[nums[l]]==0:
                del dic[nums[l]]
            dic[nums[idx]] += 1
            res.append(len(dic))
            l += 1
            idx += 1
        return res
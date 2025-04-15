class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        dic = {0:-1}
        currSum = 0
        res = 0
        for i in range(len(nums)):
            currSum += nums[i]
            compl = currSum - k
            if compl in dic:
                res = max(res, i - dic[compl])
            if currSum not in dic:
                dic[currSum] = i
        return res

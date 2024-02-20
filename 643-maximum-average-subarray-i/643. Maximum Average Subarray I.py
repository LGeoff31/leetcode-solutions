class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1: return nums[0]

        currLastIdx = 0
        nextLastIdx = 1
        currSum = 0
        for i in range(k):
            currSum += nums[i]

        res = currSum / k
        print(res)

        for i in range(k, len(nums)):
            currSum += nums[i]
            currSum -= nums[currLastIdx]
            currLastIdx += 1
            print(currSum)
            res = max(res, currSum / k)
            
        return res
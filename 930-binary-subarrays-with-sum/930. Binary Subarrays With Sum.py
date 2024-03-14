class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        currSum = 0
        freq = {}

        for num in nums:
            currSum += num
            if currSum == goal:
                res += 1
            if currSum - goal in freq: 
                res += freq[currSum - goal]
            freq[currSum] = 1 + freq.get(currSum, 0)
        return res
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        zeroFound = 0
        lastConsectiveOnes = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if zeroFound:
                    curr = lastConsectiveOnes
                    lastConsectiveOnes = 0
                    zeroFound = True
                    curr += 1
                else:
                    zeroFound = True
                    lastConsectiveOnes = 0
                    curr += 1
            else:
                curr += 1
                lastConsectiveOnes += 1
            res = max(res, curr)
        return res

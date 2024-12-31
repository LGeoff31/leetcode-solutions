class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r
        def canSplit(largest):
            subarray = 0
            currSum = 0
            for i in range(len(nums)):
                currSum += nums[i]
                if currSum > largest:
                    subarray+=1
                    currSum = nums[i]
            
            return subarray + 1 <= k
        while l <= r:
            mid = (l+r) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res             

        


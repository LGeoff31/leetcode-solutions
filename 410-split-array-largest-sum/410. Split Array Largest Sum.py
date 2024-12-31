class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = 0, sum(nums)
        def possible(target):
            currSum = 0
            idx = 0
            numArrays = 1
            while idx < len(nums):
                if currSum + nums[idx] <= target:
                    currSum += nums[idx]
                else:
                    # Start new
                    numArrays += 1
                    currSum = 0
                    currSum += nums[idx]
                    # Edge case
                    if currSum > target: return False
                idx += 1
            return numArrays <= k

        while l <= r:
            mid = (l + r) // 2
            print(mid, possible(mid))
            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
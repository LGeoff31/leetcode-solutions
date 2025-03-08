class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Binary search to see if mid avg value is achievable
        l, r = min(nums), max(nums)
        if l == r:
            return l
        res = 0
        def valid(mid):
            prev = 0
            prevMin = 0
            curr = 0
            for i in range(k):
                curr += nums[i] - mid
            idx = k
            if curr >= 0: return True
            while idx < len(nums):
                curr += nums[idx] - mid
                prev += mid - nums[idx - k]
                prevMin = max(prevMin, prev)
                if curr + prevMin >= 0:
                    return True
                idx += 1
            return False

        error = 1e-5
        while r - l > error:   
            mid = (l + r) / 2
            print('trying', mid, valid(mid))
            if valid(mid): # this value was achievable
                res = max(res, mid)
                l = mid
            else:
                r = mid
        
        return res
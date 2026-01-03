class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        res = 1e9
        l, r = 0, 0
        window = defaultdict(int)
        currSum = 0
        while r < len(nums):

            # EXTEND R WHILE NOT VALID
            while r < len(nums) and currSum < k:
                if nums[r] not in window:
                    currSum += nums[r]
                window[nums[r]] += 1
                r += 1
            
            if currSum < k: break

            res = min(res, r-l)
            window[nums[l]] -= 1
            if window[nums[l]] == 0:
                currSum -= nums[l]
                del window[nums[l]]

            l += 1
        
        while l < len(nums):
            if currSum >= k:
                res = min(res, r-l)
            window[nums[l]] -= 1
            if window[nums[l]] == 0:
                currSum -= nums[l]
                del window[nums[l]]
            l += 1


        return res if res != 1e9 else -1
            

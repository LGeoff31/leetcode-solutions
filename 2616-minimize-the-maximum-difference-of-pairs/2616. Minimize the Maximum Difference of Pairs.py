class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, nums[-1] - nums[0] # max diff
        while l < r:
            mid = (l+r) // 2
            count = 0
            i = 1
            while i < n and count < p: # p is numebr pairs we need construct
                if nums[i] - nums[i-1] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            # Greedy algorithm above that checks if there are p pairs that will satisfy a maximum difference mid
            if count >= p: # Good we found enough
                r = mid
            else:
                l = mid + 1
        return l 
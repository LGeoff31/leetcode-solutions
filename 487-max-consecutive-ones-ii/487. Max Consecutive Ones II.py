class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeroFound = False
        l, r = 0, 0
        res = 0
        count = 0
        global_count = 0
        while r < len(nums):
            if nums[r] == 0 and zeroFound:
                # Must remove that 0
                while l < len(nums) and nums[l] != 0:
                    l += 1
                    count -= 1
                # zeroFound = False
                l += 1
            elif nums[r] == 0:
                zeroFound = True
                count += 1
            else:
                count += 1
            r += 1
            global_count = max(global_count, count)
            print(count)
        return global_count

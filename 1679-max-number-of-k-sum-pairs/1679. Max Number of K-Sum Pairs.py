class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #[1,3,3,3,4]
        l, r = 0, len(nums) - 1
        count = 0
        nums.sort()
        while l < r:
            if nums[l] + nums[r] == k:
                l += 1
                r -= 1
                count += 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return count

        
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        nums = [abs(n) for n in nums]
        nums.sort()
        res = 0

        move_left = True

        while i <= j:
            if move_left:
                res += nums[j] ** 2
                j -= 1
            else:
                res -= nums[i] ** 2
                i += 1
            move_left = not move_left
            print(res)
        return res
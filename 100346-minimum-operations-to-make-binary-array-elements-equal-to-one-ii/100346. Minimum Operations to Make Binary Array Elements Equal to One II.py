class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        toggle = []
        for i in range(len(nums)):
            #check if current has been toggled -> odd amount toggles prior
            if bisect.bisect_left(toggle, i) % 2 == 1: #off number
                nums[i] = not nums[i]
            if not nums[i]:
                res += 1
                toggle.append(i)
        return res


        
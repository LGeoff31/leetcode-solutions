class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        res = []
        if nums[0] == 1:
            res.append(1)
        curr_lcm = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == 1:
                res.append(1)
                i += 1
                continue
            if curr_lcm == 1:
                curr_lcm = nums[i]
            while i < len(nums) and gcd(curr_lcm, nums[i]) > 1:
                curr_lcm = lcm(curr_lcm, nums[i])
                i += 1
            while res and gcd(res[-1], curr_lcm) > 1:
                curr_lcm = lcm(curr_lcm, res.pop())

            res.append(curr_lcm)
            # print(res)
            if i >= len(nums): break
            curr_lcm = nums[i]            
            
        return res
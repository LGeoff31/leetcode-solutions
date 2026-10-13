class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        """
        [1,1,1,1]

        [1,1,0,0]

        [0,0,0,1]

        either longest subarr or 0's or 1's

        [1, 1]
        subarr length == n + 1 and sum(subarr) - 
        subarr should have all same values

        largest seq of 0's OR multiple n 1's + 1
        or multiple n 2's + 1

        [1,1,0,0]

        [9, 9, 9, 9, 9, 9, 6, 0]

        [9, 9, 9, 9, 9], k = 18 
        4 -> 3
        5 -> 4

        [0, 0, 37, 37, 37, 37, 37, 0, 0, 0]
        """
        nums = [n % k for n in nums]
        res = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                curr += 1
                # if (curr - 1) % k == 0:
                #     res = max(res, curr)
                if nums[i] > 0 and (nums[i] * (curr - 1)) % k == 0:
                    res = max(res, curr)
            else:
                curr = 1
        print(res)
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] and nums[i-1] == 0:
                curr += 1
            else:
                curr = 1
            res = max(res, curr)
        return res
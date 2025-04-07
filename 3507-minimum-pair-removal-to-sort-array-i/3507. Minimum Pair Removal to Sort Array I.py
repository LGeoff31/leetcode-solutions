class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        def non_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True 

        while not non_decreasing(nums):
            min_sum = 1e9
            min_idx = -1
            for i in range(1, len(nums)):
                if nums[i] + nums[i-1] < min_sum:
                    min_sum = nums[i] + nums[i-1]
                    min_idx = i-1

            nums_copy = []
            idx = 0
            while idx < len(nums):
                if idx == min_idx:
                    nums_copy.append(nums[idx] + nums[idx + 1])
                    idx += 2
                else:
                    nums_copy.append(nums[idx])
                    idx += 1
                    
            nums = nums_copy
            res += 1
            print(nums, min_idx)
        return res
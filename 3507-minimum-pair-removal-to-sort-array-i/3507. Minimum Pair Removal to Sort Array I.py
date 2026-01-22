class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        cnt = 0
        while nums != sorted(nums):
            nums_copy = []
            min_pair_sum = min(nums[i] + nums[i+1] for i in range(len(nums) - 1))
            i = 0
            found = False
            while i < len(nums):
                if i+1 < len(nums) and nums[i] + nums[i+1] == min_pair_sum and not found:
                    nums_copy.append(nums[i] + nums[i+1])
                    i += 1
                    found = True
                else:
                    nums_copy.append(nums[i])
            
                i += 1
            
            nums = nums_copy
            cnt += 1
        return cnt
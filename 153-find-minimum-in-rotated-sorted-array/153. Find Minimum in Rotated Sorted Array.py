class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        #about empty arrays or length 1
        if len(nums) == 1:
            return nums[0]
        while True:
            #perfectly partitioned scenario
            partition = (left + right) // 2
            if nums[0] <= nums[partition] and nums[partition+1] <= nums[-1]:
                return min(nums[0], nums[partition+1])
            elif nums[0] > nums[partition]: #left side needs partitioned
                right = partition
                pass
            elif nums[partition+1] > nums[-1]: #right side needs partitioned
                left = partition + 1
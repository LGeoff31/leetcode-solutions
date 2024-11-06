class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def valid(a,b):
            return bin(a)[2:].count("1") == bin(b)[2:].count("1")
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j+1] and valid(nums[j], nums[j+1]):
                    print('swap', nums[i], nums[j])
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            print(nums)
        print(nums)
        return nums == sorted(nums)




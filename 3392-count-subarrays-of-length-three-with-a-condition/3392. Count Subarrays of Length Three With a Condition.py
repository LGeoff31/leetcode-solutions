class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i ,len(nums)):
                subarr = nums[i:j+1]
                if len(subarr) == 3 and 2*(subarr[0] + subarr[2]) == subarr[1]:
                    res += 1
        return res
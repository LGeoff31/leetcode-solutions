class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 3: return 4
        if n == 2: return 2
        if n == 1: return 1
        # reach eleemnts from 1-n can be made , since do same element 3 times
        # if you take the largest number, if it is just a 2*n, answer is n, otherwise n+1
        # if log2(n).is_integer():
        #     return n
        # return n+1
        highest_power_2 = 0
        for i in range(len(nums)):
            if log2(nums[i]).is_integer():
                highest_power_2 = max(highest_power_2, nums[i])
        count = 0
        for i in range(len(nums)):
            count += nums[i] > highest_power_2
        return 2 * highest_power_2
        # return 2 ** (highest_power_2-1) 
            
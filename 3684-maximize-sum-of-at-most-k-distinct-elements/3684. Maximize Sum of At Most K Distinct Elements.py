class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        res = []
        nums = sorted(list(set(nums)))
        print(nums)
        return list(reversed(nums[max(len(nums)-k,0):]))
        # return res
        # return sum(list(set(nums))[:-k])
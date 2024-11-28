class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = 1e9
        for size in range(l, r+1):
            for i in range(len(nums)):
                for j in range(i, i+size):
                    subarr = nums[i:j+1]
                    # print(subarr)
                    if len(subarr) >= l and sum(subarr) > 0:
                        res = min(res, sum(subarr))
        return res if res != 1e9 else -1
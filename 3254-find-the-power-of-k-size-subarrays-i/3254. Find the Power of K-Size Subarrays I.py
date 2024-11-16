class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def increasing(nums):
            for i in range(1, len(nums)):
                if nums[i] != nums[i-1] + 1:
                    return False
            return True
        lst = []
        for i in range(len(nums) - k + 1):
            res = 0
            subarr = nums[i: i + k]
            if increasing(subarr):
                res = max(subarr)
            if res == 0:
                lst.append(-1)
            else:
                lst.append(res)
        return lst
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]
                lst = []
                for k in range(len(nums)):
                    if not (i <=k<=j):
                        lst.append(nums[k])
                if lst == sorted(lst) and len(lst) == len(set(lst)): res += 1
        return res

        
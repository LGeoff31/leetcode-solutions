class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lst = [nums[0]]

        for i, n in enumerate(nums[1:]):
            if n > lst[-1]:
                lst.append(n)
            else:
                idx = bisect_left(lst, n)
                lst[idx] = n

        return len(lst)
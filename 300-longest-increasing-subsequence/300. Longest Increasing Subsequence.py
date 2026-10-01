class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lst = [nums[0]]

        for n in nums[1:]:
            if n > lst[-1]:
                lst.append(n)
            else:
                idx = bisect_left(lst, n)
                lst[idx] = n

        return len(lst)
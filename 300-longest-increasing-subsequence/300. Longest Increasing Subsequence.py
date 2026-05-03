class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        [2,5,6]
        """
        lst = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > lst[-1]:
                lst.append(nums[i])
            else:
                idx = bisect_left(lst, nums[i])
                lst[idx] = nums[i]

        return len(lst)

        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lst = [nums[0]]
        for num in nums:
            if num > lst[-1]:
                lst.append(num)
            else:
                lst[bisect.bisect_left(lst, num)] = num
        return len(lst)
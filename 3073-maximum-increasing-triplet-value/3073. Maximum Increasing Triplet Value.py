from sortedcontainers import SortedList
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        left = SortedList()
        right = SortedList()
        left.add(nums[0])
        for i in range(2, len(nums)):
            right.add(nums[i])

        res = 0

        for i in range(1, len(nums) - 1):
            if left[0] >= nums[i]: # Bigger than biggest element
                largest_on_left = -1e9
            else:
                largest_on_left = left[bisect.bisect_left(left, nums[i]) - 1]
            if right[-1] <= nums[i]:
                largest_on_right = -1e9
            else:
                largest_on_right = right[-1]
            res = max(res, largest_on_left + largest_on_right - nums[i])
            print(largest_on_left, largest_on_right)
            left.add(nums[i])
            right.remove(nums[i+1])
        return res
from sortedcontainers import SortedList
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False

        leftPrefix = [nums[0]]
        for i in range(1, len(nums)):
            leftPrefix.append(min(leftPrefix[i-1], nums[i]))
        rightPrefix = SortedList()
        rightPrefix.add(nums[-1])
        for i in range(len(nums) - 2, -1, -1):
            # Assume nums[i] represents 3
            if leftPrefix[i] < nums[i]:
                # Looking for number x, leftPrefix[i] < x < nums[i]
                if bisect_left(rightPrefix, nums[i]) == bisect_right(rightPrefix, leftPrefix[i]):
                    rightPrefix.add(nums[i])
                    continue
                if not(nums[i] <= rightPrefix[0] and leftPrefix[i] <= rightPrefix[0] or nums[i] >= rightPrefix[-1] and leftPrefix[i] >= rightPrefix[-1]):
                    print(i, rightPrefix, leftPrefix[i], nums[i])
                    return True
            rightPrefix.add(nums[i])
            
        return False

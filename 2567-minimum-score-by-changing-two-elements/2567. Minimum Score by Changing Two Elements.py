from copy import copy
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        """
        [4,4,5,7,7]

        want to minimize score
        - max diff b/w two: 3
        - min diff b/w two: 0

        [25,31,65,72,74,79]

        OPTION 1: Change first and last

        OPTION 2: change first two

        OPTION 3: change last two

        take the MIN b/w the three options
        """
        nums.sort()

        # OPTION ONE
        nums_copy = copy(nums)
        nums_copy[0] = nums_copy[1]
        nums_copy[-1] = nums_copy[-2]
        OPTION_ONE = (nums_copy[-1] - nums_copy[0])

        # OPTION TWO
        nums_copy = copy(nums)
        nums_copy[0] = nums_copy[2]
        nums_copy[1] = nums_copy[2]
        OPTION_TWO = nums_copy[-1] - nums_copy[0]

        # OPTION THREE
        nums_copy = copy(nums)
        nums_copy[-1] = nums_copy[-3]
        nums_copy[-2] = nums_copy[-3]
        OPTION_THREE = nums_copy[-1] - nums_copy[0]

        return min(OPTION_ONE, OPTION_TWO, OPTION_THREE)









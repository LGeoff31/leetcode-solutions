class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if nums[1] <= nums[0]: return False
        a = [1]

        for i in range(2, len(nums)):
            if nums[i] > nums[i-1]:
                if a[-1] != 1:
                    a.append(1)
            elif nums[i] < nums[i-1]:
                if a[-1] != -1:
                    a.append(-1)
            else: return False
        print(a)
        return a == [1,-1,1]
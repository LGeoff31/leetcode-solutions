class Solution:
    def findScore(self, nums: List[int]) -> int:
        lst = []
        res = 0
        for i in range(len(nums)):
            if not lst or nums[i] < lst[-1]:
                lst.append(nums[i])
            else:
                while lst:
                    res += lst.pop()
                    if lst:
                        lst.pop()

        while lst:
            res += lst.pop()
            if lst:
                lst.pop()
        return res
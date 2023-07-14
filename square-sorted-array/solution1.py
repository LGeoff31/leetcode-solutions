class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = []
        for num in nums:
            lst.append(num*num)
        lst.sort()
        return lst

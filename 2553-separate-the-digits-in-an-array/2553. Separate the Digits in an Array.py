class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(c) for n in nums for c in str(n)]
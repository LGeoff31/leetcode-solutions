class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda n: (int(bin(n)[2:][::-1], 2), n))
        return nums
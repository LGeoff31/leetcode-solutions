class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        product = 1
        for n in nums:
            product *= n
        return target ** 2 == product
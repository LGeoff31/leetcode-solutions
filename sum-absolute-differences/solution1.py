class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            total = 0
            for j in nums:
                total += abs(i - j)
            result.append(total)

        return result

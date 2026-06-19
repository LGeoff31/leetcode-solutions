class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(list(accumulate([0] + gain)))

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(Counter(candyType)), len(candyType) // 2)
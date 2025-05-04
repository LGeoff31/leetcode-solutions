class Solution:
    def maxProduct(self, n: int) -> int:
        lst = [int(num) for num in str(n)]
        lst.sort()
        return lst[-1] * lst[-2]
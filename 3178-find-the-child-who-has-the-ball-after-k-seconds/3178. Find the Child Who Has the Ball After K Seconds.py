class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cycle = 2 * (n-1)
        lst = list(range(n))
        k %= cycle
        if k <= (n-1):
            return k
        else:
            return 2*(n-1) - k
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        cycle = 2 * (n-1)
        lst = list(range(n))
        k %= cycle
        #only forward
        if k <= (n-1):
            return lst[k]
        else:
            return lst[2*(n-1) - k]
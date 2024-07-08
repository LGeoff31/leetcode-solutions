class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        start = 0
        lst = list(range(1, n+1))
        while n > 1:
            start = (start + (k-1)) % n
            lst.pop(start)
            n -= 1
        
        return lst[0]
        
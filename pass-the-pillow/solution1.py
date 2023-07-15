class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = 2 * (n-1)
        time %= cycle
        print(time)
        i = 1
        if 1 + time > n:
            return 2*n - 1 - time
        return 1 + time

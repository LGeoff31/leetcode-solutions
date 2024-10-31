class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7      
        prev = 1
        curr = 1
        
        def size(i):
            ans = 0
            while i != 0:
                ans += 1
                i //= 2
            return ans
        for i in range(2, n+1):
            curr = ((prev << size(i)) + (i)) % MOD
            prev = curr

        return curr % MOD
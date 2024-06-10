class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        lst = [1] * n
        for i in range(k): #O(K)
            lst = list(accumulate(lst)) #O(N)
        return lst[-1] % MOD
        
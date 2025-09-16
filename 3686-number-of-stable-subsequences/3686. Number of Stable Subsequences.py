from typing import List

class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        # c1[p]: ends with parity p (0 even, 1 odd), last run length = 1
        # c2[p]: ends with parity p, last run length = 2
        c1 = [0, 0]
        c2 = [0, 0]

        for x in nums:
            p = x & 1
            # New sequences that TAKE this x:
            # - Start new or switch parity -> run length 1
            new_c1 = (c1[1 - p] + c2[1 - p] + 1) % MOD
            # - Extend same-parity run of length 1 -> becomes length 2
            new_c2 = c1[p]

            # Add them to pools (skip is implicit by not changing the opposite pools)
            c1[p] = (c1[p] + new_c1) % MOD
            c2[p] = (c2[p] + new_c2) % MOD

        return (c1[0] + c1[1] + c2[0] + c2[1]) % MOD

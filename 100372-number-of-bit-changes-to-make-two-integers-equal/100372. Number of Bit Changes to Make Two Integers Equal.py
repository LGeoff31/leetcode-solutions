class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n < k:
            return -1

        if (n | k) != n:
            return -1

        differing_bits = n ^ k
        
        changes_needed = bin(differing_bits).count('1')
        
        return changes_needed
            
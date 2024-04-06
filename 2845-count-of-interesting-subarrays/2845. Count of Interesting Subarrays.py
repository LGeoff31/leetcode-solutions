class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = prefix = 0 
        freq = Counter({0 : 1})
        for x in nums: 
            if x % modulo == k: prefix += 1
            prefix %= modulo
            ans += freq[(prefix-k) % modulo]
            freq[prefix] += 1
        return ans 
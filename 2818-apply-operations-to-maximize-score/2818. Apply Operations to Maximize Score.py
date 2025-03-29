class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7

        left = [-1] * len(nums)
        right = [len(nums)] * len(nums)
        spf = list(range(max(nums) + 1))
        for i in range(2, int(max(nums) ** 0.5) + 1):
            if spf[i] == i:  # i is a prime
                for j in range(i * i, max(nums) + 1, i):
                    if spf[j] == j:  # Mark the smallest prime factor
                        spf[j] = i
        def p_count(num): # O(N * sqrt(N))
            unique_primes = set()
            while num > 1:
                unique_primes.add(spf[num])
                num //= spf[num]
            return len(unique_primes)
        
        def quick_exp(base, exp):
            res = 1
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res % MOD


        prime_count = [p_count(num) for num in nums]

        # Populate left
        i = 0
        stack = []
        while i < len(nums):
            while stack and prime_count[i] > stack[-1][0]:
                stack.pop()
            if stack:
                val, idx = stack[-1]
                left[i] = idx
            stack.append((prime_count[i], i))
            i += 1

        # Populate right
        i = 0
        stack = []
        while i < len(nums):
            while stack and prime_count[i] > stack[-1][0]:
                val, idx = stack.pop()
                right[idx] = i
            stack.append((prime_count[i], i))
            i += 1

        sorted_list = sorted([(nums[i], i) for i in range(len(nums))], reverse=True)
        res = 1
        i = 0
        while k > 0:
            val, idx = sorted_list[i]
            possibilities_with_val = ((idx - left[idx]) * (right[idx] - idx))
            if possibilities_with_val > k:
                res = (res * quick_exp(val, k)) % MOD
                break
            k -= possibilities_with_val
            res = (res * quick_exp(val, possibilities_with_val)) % MOD
            i += 1

        return res % MOD
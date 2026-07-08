class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        def get_prefix_sum(s):
            prefix = []
            curr = 0
            for n in s:
                curr += int(n)
                prefix.append(curr)
            return prefix
        
        def get_prefix_digits(s):
            prefix = []
            for n in s:
                if n != '0':
                    if not prefix:
                        prefix.append(int(n))
                    else:
                        prefix.append((prefix[-1] * 10 + int(n)) % MOD)  # <-- mod added here
            return prefix
        
        def get_number_non_zero(s):
            prefix = [] 
            cnt = 0
            for n in s:
                cnt += n != '0'
                prefix.append(cnt)
            return prefix

        prefix_sum = get_prefix_sum(s)
        prefix_digts = get_prefix_digits(s)
        prefix_non_zero = get_number_non_zero(s)

        # precompute powers of 10 mod MOD, up to total count of non-zero digits
        pow10 = [1] * (len(prefix_digts) + 1)
        for i in range(1, len(pow10)):
            pow10[i] = (pow10[i-1] * 10) % MOD

        res = []
        for start, end in queries:
            digit_sum = prefix_sum[end] - (prefix_sum[start-1] if start > 0 else 0)
            if prefix_non_zero[end] == 0:
                res.append(0)
                continue

            number_preceeding_nonzeros = prefix_non_zero[start-1] if start > 0 else 0
            end_count = prefix_non_zero[end]

            if end_count == number_preceeding_nonzeros:
                res.append(0)
                continue

            full_prefix_number = prefix_digts[end_count - 1]
            preceeding_number = prefix_digts[number_preceeding_nonzeros - 1] if number_preceeding_nonzeros > 0 else 0
            k = end_count - number_preceeding_nonzeros

            substring_number = (full_prefix_number - preceeding_number * pow10[k]) % MOD
            res.append(substring_number * digit_sum % MOD)

        return res
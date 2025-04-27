"""
NcR = N! / (N-R)!R!



"""

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        dic = Counter(s)
        freq = defaultdict(int)
        for key in dic:
            freq[dic[key]] += 1
        if sum(freq.values()) < k: return 0
        lst = sorted([(key, freq[key]) for key in freq], reverse=True)
        print(lst)
        idx = 0
        res = 1
        while k > 0:
            # if idx >= len(lst): break
            amount_of_freq = lst[idx][1]
            i = min(k, amount_of_freq)
            res *= comb(amount_of_freq, i) * lst[idx][0] ** i
            idx += 1
            k -= i

        return res % MOD
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10 ** 9 + 7

        min_val = min(complexity)
        min_count = complexity.count(min_val)
        if complexity[0] != min_val:
            return 0
        if min_count > 1: return 0
        non_min_count = len(complexity) - min_count
        dic = Counter(complexity)
        res = factorial(non_min_count)

        # for key in dic:
        #     if key != min_val:
        #         res //= factorial(dic[key]) 

        return res % MOD
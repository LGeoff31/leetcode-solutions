class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        dic=Counter(power)
        power = sorted(list(set(power)))
        @cache
        def dfs(i):
            if i >= len(power):
                return 0
            # TAKE / DONT TAKE
            return max(
                dic[power[i]] * power[i] + dfs(bisect_left(power, power[i] + 3)),
                dfs(i+1)
            )

        return dfs(0)


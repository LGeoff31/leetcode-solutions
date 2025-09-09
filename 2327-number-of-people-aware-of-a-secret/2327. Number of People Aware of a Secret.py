class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        aware, spread, total = [0] * n, 0, 1
        aware[0] = 1
        for day in range(1, n):

            if day >= delay:
                spread += aware[day - delay]
            
            if day >= forget:
                f = aware[day - forget]
                total -= f
                spread -= f
            
            aware[day] = spread
            total += spread

        return total % MOD
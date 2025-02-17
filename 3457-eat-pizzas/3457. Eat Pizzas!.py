class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas) // 4
        if n == 1: return max(pizzas)
        pizzas.sort()
        print(pizzas)
        even_days = n // 2
        odd_days = n - even_days
        res = sum(pizzas[len(pizzas) - odd_days:])
        idx = len(pizzas) - odd_days - 2
        while even_days != 0:
            res += pizzas[idx]
            idx -= 2
            even_days -= 1
        return res
        # return res + pizzas[len(pizzas) - n - 1]
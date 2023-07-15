class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        minimum = 1e9
        for price in prices:
            minimum = min(price, minimum)
        prices.remove(minimum)
        min_2 = 1e9
        for price in prices:
            min_2 = min(min_2, price)
        if min_2 + minimum > money:
            return money
        return money - min_2 - minimum

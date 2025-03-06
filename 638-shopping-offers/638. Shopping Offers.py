class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.res = 1e9
        def any_negative(needs): # -1, 0, 1
            for num in needs:
                if num < 0: 
                    return -1
            return sum(needs)
        def dfs(needs, cost):
            val = any_negative(needs)
            if val == -1 or cost > self.res:
                return 1e9
            if val == 0:
                self.res = min(self.res, cost)
                return
            # Try using only price
            c = 0
            for i in range(len(needs)):
                c += needs[i] * price[i]
            dfs([0], cost + c)

            # Try each of the special offers
            for i in range(len(special)):
                n = needs.copy()
                print('n', n, special[i])
                for j in range(len(special[i]) - 1):
                    n[j] -= special[i][j]
                dfs(n, cost + special[i][-1])

        dfs(needs, 0)
        return self.res

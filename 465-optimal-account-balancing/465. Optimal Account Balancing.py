class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # 0: -5
        # 1: 10
        # 2: -5


        # 0: -4
        # 1: 4
        # 2: 0
        dic = defaultdict(int)
        for a, b, amount in transactions:
            dic[a] -= amount
            dic[b] += amount
        balance_amount = [amount for amount in dic.values() if amount]
        n = len(balance_amount)
        print(balance_amount)
        def dfs(curr): # balance_amount[curr:] still need empty 
            while curr < n and balance_amount[curr] == 0:
                curr += 1
            if curr == n:
                return 0
            cost = 1e9
            for nxt in range(curr + 1, n):
                if balance_amount[curr] * balance_amount[nxt] < 0:
                    # Different signs, 
                    balance_amount[nxt] += balance_amount[curr]
                    cost = min(cost, 1 + dfs(curr + 1))
                    balance_amount[nxt] -= balance_amount[curr]
            return cost

        return dfs(0)

        # If you want minimum transactions possible, when you give someone your positive money, ideally you want to clear there debt immediately

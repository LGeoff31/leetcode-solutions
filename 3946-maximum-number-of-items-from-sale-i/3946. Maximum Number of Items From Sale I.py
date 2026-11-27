class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        """
        you can get 3 pairs for 5,  budget = 8
        OR
        you can get 2 + 2 pairs for 8, each worth price 4
        """
        # Step 1: Create a mapping that gives you number free copies given you purchuse the ith item
        free_copies = defaultdict(int)

        for i in range(len(items)):
            for j in range(len(items)):
                if i == j:
                    continue

                if items[j][0] % items[i][0] == 0:
                    free_copies[i] += 1
        # Step 2: Do a backtracking approach, generating all possible combinations such that curr <= budget
        min_price = min(items[i][1] for i in range(len(items)))
        @cache
        def dfs(i, curr_spending): # O (N * budget)
            if i == len(items):
                return (budget - curr_spending) // min_price
            
            total_items = 0
            total_items = max(total_items, dfs(i+1, curr_spending))

            if curr_spending + items[i][1] <= budget:
                total_items = max(total_items, 1 + free_copies[i] + dfs(i+1, curr_spending + items[i][1]))
            return total_items
        
        res = dfs(0, 0)
        dfs.cache_clear()
        return res

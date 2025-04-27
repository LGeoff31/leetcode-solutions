class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # Binary search
        # Heap
        # Net + Sorting
        # DP?
        positive_ev = []
        negative_ev = []

        for cost, cashback in transactions:
            if cost > cashback:
                negative_ev.append((cost, cashback))
            else:
                positive_ev.append((cost, cashback))
        
        positive_ev.sort(reverse=True)
        negative_ev = sorted(negative_ev, key = lambda x: x[1])
        if not negative_ev:
            return positive_ev[0][0]
        res = 0
        for cost, cashback in negative_ev[:-1]:
            res += cost - cashback
        res += negative_ev[-1][0]
        print(res)
        if positive_ev and negative_ev[-1][1] < positive_ev[0][0]:
            return positive_ev[0][0] - negative_ev[-1][1] + res
        return res
        # print(positive_ev)
        # print(negative_ev)
        # return 
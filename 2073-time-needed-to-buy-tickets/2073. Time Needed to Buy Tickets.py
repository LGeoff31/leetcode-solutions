class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        n = len(tickets)
        while tickets[k] != 0:
            for i in range(n):
                if tickets[i] != 0:
                    res+=1
                    tickets[i] -= 1
                    if tickets[i] == 0 and i==k: return res
        return res
        
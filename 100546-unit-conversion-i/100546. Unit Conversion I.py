class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        res = [0] * (len(conversions) + 1)
        dic = defaultdict(list)
        for u,v,w in conversions:
            dic[u].append((v, w))
        queue = deque([[0,1]])
        while queue:
            node, quantity = queue.popleft()
            res[node] = quantity % MOD
            for nei, nei_weight in dic[node]:
                queue.append((nei,(quantity * nei_weight) % MOD))
        return res
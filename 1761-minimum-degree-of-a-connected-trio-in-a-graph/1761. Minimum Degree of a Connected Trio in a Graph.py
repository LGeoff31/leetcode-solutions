class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # Let's say a connceted component has n nodes. If there # of edges > n, then  
        dic = defaultdict(set)
        for u,v in edges:
            dic[u].add(v)
            dic[v].add(u)
        print(dic)
        res = 1e9
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1,n+1):
                    if j in dic[i] and j in dic[k] and k in dic[i] and k in dic[j]:
                        res = min(res, len(dic[i]) + len(dic[j]) + len(dic[k]) - 6)
        return res if res != 1e9 else -1
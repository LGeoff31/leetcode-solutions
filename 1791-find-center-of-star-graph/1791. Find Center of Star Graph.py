class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = defaultdict(list)
        n = len(edges) + 1
        for u, v in edges:
            dic[u].append(v)
            dic[v].append(u)
        lst = [False] * n
        for key in dic:
            if len(dic[key]) == n-1:
                return key

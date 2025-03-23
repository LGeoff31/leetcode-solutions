class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        res = 0
        dic = defaultdict(list)
        n = len(properties)
        def valid(i, j):
            count = 0
            arr1 = list(set(properties[i]))
            arr2 = set(properties[j])
            for num in arr1:
                if num in arr2:
                    count += 1
            return count >= k
            
        for i in range(n):
            for j in range(i+1, n):
                if valid(i, j):
                    dic[i].append(j)
                    dic[j].append(i)
        visited = set()
        def dfs(node):
            for nei in dic[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
                    
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
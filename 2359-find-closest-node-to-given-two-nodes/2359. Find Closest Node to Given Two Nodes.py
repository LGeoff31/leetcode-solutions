class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = {}
        for i in range(len(edges)):
            adj[i] = edges[i]

        def bfs(node):
            arr = []
            visited = set()
            while True:
                if node not in adj:
                    break
                if node in visited:
                    break
                visited.add(node)
                arr.append(node)
                node = adj[node]

            return arr
        
        arr1 = bfs(node1)
        arr2 = bfs(node2)
        print(arr1, arr2)
        a,b = set(arr1), set(arr2)
        res = 1e9
        ans = -1
        x,y = {num : i for i, num in enumerate(arr1)}, {num : i for i, num in enumerate(arr2)}
        for i, num in enumerate(arr1):
            if num in b:
                if max(i, y[num]) <= res:
                    if max(i, y[num]) == res:
                        if num < ans:
                            ans = num
                    else:
                        ans = num
                    res = max(i, y[num])
        for i, num in enumerate(arr2):
            if num in a:
                if max(i, x[num]) <= res:
                    if max(i, x[num]) == res:
                        if num < res:
                            ans = num
                    else:
                        ans = num
                    res = max(i, x[num])
            
        return ans
       
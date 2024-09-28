class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # Brute force: From node 0, dfs to neighboring nodes, and from those dfs
        # Base case: If get back to node 0, return sum all nodes in visited set
        # If the sum ever is above maxTime, return
        # Return the maximum sum from all the path traversals

        adj1 = {}
        adj2 = defaultdict(list)

        
        for u,v,time in edges:
            adj1[(u,v)] = time
            adj1[(v,u)] = time

            adj2[u].append(v)
            adj2[v].append(u)
        self.res = 0
        def dfs(root, t, visited, currSum):
            if t > maxTime:
                return
            if root == 0:
                # nonlocal res
                self.res = max(self.res, currSum)
            visited.add(root)
            for nei in adj2[root]:
                if nei not in visited:
                    dfs(nei, t+adj1[(root, nei)], set(visited), currSum + values[nei])
                else:
                    dfs(nei, t+adj1[(root, nei)], set(visited), currSum)
        dfs(0, 0, set(), values[0])
        return self.res
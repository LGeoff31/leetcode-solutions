class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Since nodes are numbers 0 to n-1, there all unique
        # For each node, have a helper function that gives you all nodes that can be reached from it
        # With that list, determine if it is a fully connected component, if so, increment res
        visited = set()
        dic = defaultdict(list)
        for u,v in edges:
            dic[u].append(v)
            dic[v].append(u)
        res = 0
        print(dic)
        def find_neighbors(node):
            res = [node]
            queue = deque([node])
            while queue:
                node = queue.popleft()
                print('reached', node)
                for nei in dic[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
                        res.append(nei)
            return res

        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                arr = find_neighbors(i)
                print(arr)
                valid = True
                for j in range(len(arr)):
                    # Ensure that arr[k] exists in dic[arr[j]] for all k, k!=j, otherwise return False and not increment res
                    for k in range(len(arr)):
                        if j != k:
                            if arr[k] not in dic[arr[j]]:
                                valid = False
                res += valid

        return res
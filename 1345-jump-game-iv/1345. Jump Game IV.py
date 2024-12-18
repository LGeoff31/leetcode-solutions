class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dic = defaultdict(list)
        for i, val in enumerate(arr):
            dic[val].append(i)
        
        queue = deque([0])
        visited = {0}
        move = 0
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == len(arr) - 1:
                    return move
            
                for nei in dic[arr[node]]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
                
                # Clear processed value indices to prevent revisiting
                dic[arr[node]].clear()
                
                if node + 1 < len(arr) and node + 1 not in visited:
                    visited.add(node + 1)
                    queue.append(node + 1)
                if node - 1 >= 0 and node - 1 not in visited:
                    visited.add(node - 1)
                    queue.append(node - 1)
            
            move += 1
        
        return 0

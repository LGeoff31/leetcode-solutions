class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        incoming = [0] * n  
        suspicious = [False] * n  

        # Build the graph and count incoming edges
        for invocation in invocations:
            graph[invocation[0]].append(invocation[1])
            incoming[invocation[1]] += 1

        # Mark suspicious methods starting from k
        self.markSuspiciousMethods(graph, suspicious, k)

        # Check for non-suspicious methods with suspicious neighbors
        for i in range(n):
            if not suspicious[i]: 
                for neighbor in graph[i]:
                    if suspicious[neighbor]:
                        return list(range(n))  # Return all methods if any neighbor is suspicious

        # Collect and return non-suspicious methods
        result = [i for i in range(n) if not suspicious[i]]
        return result

    def markSuspiciousMethods(self, graph: List[List[int]], suspicious: List[bool], k: int):
        stk = [k]
        suspicious[k] = True
        
        while stk:
            method = stk.pop()
            
            for neighbor in graph[method]:
                if not suspicious[neighbor]:
                    suspicious[neighbor] = True
                    stk.append(neighbor)
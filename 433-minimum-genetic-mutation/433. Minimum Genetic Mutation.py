class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set()
        queue = deque([startGene])

        def diff(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]: count+=1
            return count
        moves = 0
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word not in visited:
                    if word == endGene: return moves
                    for j in bank:
                        if diff(word, j) == 1:
                            queue.append(j)
                    visited.add(word)
            moves+=1
            

        return -1
        
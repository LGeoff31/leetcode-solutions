class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        idx_max_player = skills.index(max(skills))
        # Simulate
        players = len(skills)
        queue = deque([_ for _ in range(players)])
        win_counts = [0] * players
        while True:
            if queue[0] == idx_max_player or queue[1] == idx_max_player:
                break
            if skills[queue[0]] < skills[queue[1]]:
                win_counts[queue[1]] += 1
                if win_counts[queue[1]] == k:
                    return queue[1]
                queue.append(queue.popleft())
            else:
                win_counts[queue[0]] += 1
                if win_counts[queue[0]] == k:
                    return queue[0]
                queue[0], queue[1] = queue[1], queue[0]
                queue.append(queue.popleft())
            
        return idx_max_player
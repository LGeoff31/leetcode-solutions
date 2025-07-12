class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer, secondPlayer = firstPlayer - 1, secondPlayer - 1
        @cache
        def dfs(round, mask):
            queue = deque()
            # Add all players into queue
            for i in range(n):
                if (1 << i) & mask:
                    queue.append(i)

            # Simulate process
            eliminated = []
            while len(queue) > 1:
                s, e = queue.popleft(), queue.pop()
                if s == firstPlayer and e == secondPlayer:
                    return [round, round]
                elif s in {firstPlayer, secondPlayer}:
                    eliminated.append([e])
                elif e in {firstPlayer, secondPlayer}:
                    eliminated.append([s])
                else:
                    eliminated.append([s, e])
            
            # Cross product for all possibilities & Remove eliminated players
            earliest, latest = 1e9, -1e9
            for eliminated_players in product(*eliminated):
                new_mask = mask
                for i in eliminated_players:
                    new_mask ^= 1 << i
                e, l = dfs(round + 1, new_mask)
                earliest = min(earliest, e)
                latest = max(latest, l)
            return [earliest, latest]
    
        return dfs(1, (1 << n) - 1)
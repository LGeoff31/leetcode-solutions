class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        def calculate_position(r, c, n):
            maxNumber = n**2 - r*n
            row = n - r - 1

            if row % 2 == 0: #ascending
                position = maxNumber - (n - c - 1)
            else: #descending
                position = maxNumber - c
            return position 

        snakesladders = defaultdict(int)
        n = len(board)

        for r in range(n):
            for c in range(n):
                if board[r][c] != -1:
                    position = calculate_position(r, c, n)
                    destination = board[r][c]
                    snakesladders[position] = destination

        queue = deque([(1,0)])
        visited = set([1])

        while queue:
            curr, count = queue.popleft()
            if curr >= n**2:
                return count 

            for next_move in range(curr + 1, min(curr + 7, n**2 + 1)):
                # Check if next_move leads to a snake or ladder.
                if next_move in snakesladders:
                    next_move = snakesladders[next_move]

                if next_move not in visited:
                    visited.add(next_move)
                    queue.append((next_move, count + 1))

        return -1
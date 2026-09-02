class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        def get_starting_position():
            for r in range(rows):
                for c in range(cols):
                    if classroom[r][c] == "S":
                        return [r, c]
            return [-1, -1]

        rows, cols = len(classroom), len(classroom[0])
        start_r, start_c = get_starting_position()

        litter_positions = []
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == "L":
                    litter_positions.append((r, c))

        litter_index = {pos : i for i, pos in enumerate(litter_positions)}
        full_mask = (1 << len(litter_positions)) - 1

        start_mask = 0
        queue = deque([(start_r, start_c, start_mask, energy)])
        seen = {(start_r, start_c, start_mask, energy)}

        steps = 0
        while queue:
            for _ in range(len(queue)):
                r, c, current_litter, current_energy = queue.popleft()
                if current_litter == full_mask:
                    return steps
                
                if current_energy <= 0:
                    continue
                
                for nei_r, nei_c in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
                    if not(0 <= nei_r < rows and 0 <= nei_c < cols):
                        continue 
                    cell = classroom[nei_r][nei_c]
                    if cell == "X":
                        continue 
                    
                    if cell == "R":
                        new_energy = energy
                    else:
                        new_energy = current_energy - 1
                    
                    if new_energy < 0:
                        continue 
                    
                    new_mask = current_litter
                    if (nei_r, nei_c) in litter_index:
                        new_mask = new_mask | (1 << litter_index[(nei_r, nei_c)])

                    state = (nei_r, nei_c, new_mask, new_energy)
                    if state not in seen:
                        seen.add(state)
                        queue.append(state)
            steps += 1

        return -1
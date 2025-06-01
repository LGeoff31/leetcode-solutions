class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        # S .
        # X L

        # L S
        # R L

        # L . S
        # R X L

        rows, cols = len(classroom), len(classroom[0])
        amount_litter = sum(l.count("L") for l in classroom)
        idx = 0
        L_map = {}
        start_r, start_c = -1, -1
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == "S":
                    start_r, start_c = r, c
                if classroom[r][c] == "L":
                    L_map[(r,c)] = idx
                    idx += 1
        l_bitstring = (1 << idx) - 1 # bit mask, help keep track of state
        queue = deque([(start_r, start_c, 0, energy, 0)]) # (r, c, litter_collected, energy)
        dic = {} # (r, c, litter) : max energy
        dic[(start_r, start_c, 0)] = energy
        while queue:
            r, c, litter, e, moves = queue.popleft()

            if classroom[r][c] == "L":
                litter |= (1 << L_map[(r,c)])
                
            if litter == l_bitstring:
                return moves

            if classroom[r][c] == "R":
                e = energy

            # BFS 4 directions
            new_energy = e-1
            for new_r, new_c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0<=new_r<rows and 0<=new_c<cols and new_energy >= 0 and ((new_r, new_c, litter) not in dic or dic[(new_r, new_c, litter)] < new_energy) and classroom[new_r][new_c] != "X":
                    dic[(new_r, new_c, litter)] = new_energy
                    # visited.add((new_r, new_c, litter, new_energy))
                    queue.append((new_r, new_c, litter, new_energy, moves+1))
        return -1
            
        # Do a BFS from starting position to try all posibilities
        
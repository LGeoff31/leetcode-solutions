class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        # Can only use letter once
        # BFS, keep track (r,c,moves,used letters)

        # Which letter is most acceptable to jump to?? Probably need to try all options

        # Try to think of this in a different way
        # Starting at the bottom right corner, find the minimum distance to get to all 26 letters or however many there are
        # That way, if we reach one of those letters in our bfs starting from the top left corner, we can instantly determine the distance to bottom right
        # Take the min of those which take letters and taking no letters are all
        # How can i find the minimum distance from start to every letter, more tricky since maybe to get to B, may be less steps if i teleport to A first
        # if matrix == [".AA.#","..G..",".HB.D","##.HB","B..FB","F.A..","E.C.H","H.H.#","CFHED"]: return 4
        # if matrix == [".C.BBA..#",".CB...BA.","AAA.#.#..","##BABCC.A","B..ACCB#A","A.#.A#..C","AC...CC..","..#.B...#","A##.#A...","...CAB..."]: return 5
        rows, cols = len(matrix), len(matrix[0])
        if matrix[rows-1][cols-1] == "#": return -1
        def distance_without_letters():
            visited = set()
            visited.add((0,0))
            queue = deque([((0, 0))])
            moves = 0
            if matrix[0][0] != '.': return 1e9
            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    if (r,c) == (rows-1,cols-1):
                        return moves
                    for new_r, new_c in [(r-1, c), (r+1,c), (r, c+1), (r, c-1)]:
                        if 0<=new_r<rows and 0<=new_c<cols and matrix[new_r][new_c] and (new_r, new_c) not in visited and matrix[new_r][new_c] != "#":
                            visited.add((new_r, new_c))
                            queue.append((new_r, new_c))
                moves += 1
            return 1e9
            
        # start_position_to_letters = {} 
        # end_position_to_letters = {} 
        
        present_letters = defaultdict(list)
        _ = [present_letters[ch].append((r, c)) for r, row in enumerate(matrix) for c, ch in enumerate(row) if ch.isalpha()]
        if not present_letters: 
            return distance_without_letters() if distance_without_letters() != 1e9 else -1
        queue = deque([(0, 0, 0)])
        visited = set()
        used_letters = set()
        # Dijkstra's idea shortest path
        min_distance = [[1e9] * cols for _ in range(rows)]
        min_distance[0][0] = 0
        while queue:
            for i in range(len(queue)):
                r,c,moves = queue.popleft()
                if (r,c) == (rows-1, cols-1):
                    return moves
                if matrix[r][c].isalpha() and matrix[r][c] not in used_letters:
                    used_letters.add(matrix[r][c])
                    for nxt_r, nxt_c in present_letters[matrix[r][c]]:
                        if moves < min_distance[nxt_r][nxt_c]:
                            min_distance[nxt_r][nxt_c] = moves
                            queue.appendleft((nxt_r, nxt_c, moves))
                     
                for nxt_r, nxt_c in [(r-1, c), (r+1, c), (r, c-1), (r,c+1)]:
                    if 0<=nxt_r<rows and 0<=nxt_c<cols and (nxt_r, nxt_c) not in visited and matrix[nxt_r][nxt_c] != "#":
                        if moves + 1 < min_distance[nxt_r][nxt_c]:
                            min_distance[nxt_r][nxt_c] = moves + 1
                            queue.append((nxt_r, nxt_c, moves + 1))
                    
        return -1
                
            
        # def start_to_letters():
        #     visited = set()
        #     visited.add((0,0))
        #     queue = deque([((0, 0, 0))])
        #     used_letters = set()
        #     while queue and used_letters != len(present_letters):
        #         for i in range(len(queue)):
        #             r,c, moves = queue.popleft()
        #             if matrix[r][c].isalpha() and matrix[r][c] not in used_letters:
        #                 if matrix[r][c] not in start_position_to_letters:
        #                     start_position_to_letters[matrix[r][c]] = moves
        #                 used_letters.add(matrix[r][c])
        #                 for nxt_r, nxt_c in present_letters[matrix[r][c]]:
        #                     if (nxt_r, nxt_c) not in visited:
        #                         visited.add((nxt_r, nxt_c))
        #                         queue.append((nxt_r, nxt_c, moves))
        #                 # if len(present_letters[matrix[r][c]]) == 1:
        #                 for new_r, new_c in [(r-1, c), (r+1,c), (r, c+1), (r, c-1)]:
        #                     if 0<=new_r<rows and 0<=new_c<cols and matrix[new_r][new_c] and (new_r, new_c) not in visited and matrix[new_r][new_c] != "#": 
        #                         visited.add((new_r, new_c))
        #                         queue.append((new_r, new_c, moves + 1))
        #             else:
        #                 for new_r, new_c in [(r-1, c), (r+1,c), (r, c+1), (r, c-1)]:
        #                     if 0<=new_r<rows and 0<=new_c<cols and matrix[new_r][new_c] and (new_r, new_c) not in visited and matrix[new_r][new_c] != "#": 
        #                         visited.add((new_r, new_c))
        #                         queue.append((new_r, new_c, moves + 1))
        # def end_to_letters():
        #     visited = set()
        #     visited.add((rows-1,cols-1))
        #     queue = deque([((rows-1, cols-1, 0))])
        #     used_letters = set()
        #     while queue and used_letters != len(present_letters):
        #         for i in range(len(queue)):
        #             r,c, moves = queue.popleft()
        #             if matrix[r][c].isalpha() and matrix[r][c] not in used_letters:
        #                 if matrix[r][c] not in end_position_to_letters:
        #                     end_position_to_letters[matrix[r][c]] = moves
        #                 used_letters.add(matrix[r][c])
        #                 for nxt_r, nxt_c in present_letters[matrix[r][c]]:
        #                     if (nxt_r, nxt_c) not in visited:
        #                         visited.add((nxt_r, nxt_c))
        #                         queue.append((nxt_r, nxt_c, moves))
        #                 # if len(present_letters[matrix[r][c]]) == 1:
        #                 for new_r, new_c in [(r-1, c), (r+1,c), (r, c+1), (r, c-1)]:
        #                     if 0<=new_r<rows and 0<=new_c<cols and matrix[new_r][new_c] and (new_r, new_c) not in visited and matrix[new_r][new_c] != "#": 
        #                         visited.add((new_r, new_c))
        #                         queue.append((new_r, new_c, moves + 1))
        #             else:
        #                 for new_r, new_c in [(r-1, c), (r+1,c), (r, c+1), (r, c-1)]:
        #                     if 0<=new_r<rows and 0<=new_c<cols and matrix[new_r][new_c] and (new_r, new_c) not in visited and matrix[new_r][new_c] != "#":
        #                         visited.add((new_r, new_c))
        #                         queue.append((new_r, new_c, moves + 1))
            
        # start_to_letters()
        # end_to_letters()
        # print(start_position_to_letters)
        # print(end_position_to_letters)
        # if sorted(start_position_to_letters.keys()) != sorted(end_position_to_letters.keys()):
        #     return -1
        min_distance_using_letters = 1e9
        for key in start_position_to_letters:
            if key in end_position_to_letters:
                min_distance_using_letters = min(min_distance_using_letters, start_position_to_letters[key] + end_position_to_letters[key])
        # print(distance_without_letters(), min_distance_using_letters)
        return min(distance_without_letters(), min_distance_using_letters) if min(distance_without_letters(), min_distance_using_letters) != 1e9 else -1
        
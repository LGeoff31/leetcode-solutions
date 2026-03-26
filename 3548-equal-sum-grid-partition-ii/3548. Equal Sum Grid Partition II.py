class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        """
        1 1 1
        9 3 2
        3 3 4
        - - - -
        2 2 3
        1 1 2
        3 9 5

        10 5 4 5

        """
        rows, cols = len(grid), len(grid[0])
        top_mapping = defaultdict(list) # val : [idx1, idx2]
        bottom_mapping = defaultdict(deque) # val : [idx1, idx2]
        total_sum = sum(grid[r][c] for r in range(rows) for c in range(cols))
        if cols == 1:
            # turn [[1], [2], [3]] -> [[1,2,3]]
            lst = []
            for r in range(rows):
                lst.append(grid[r][0])
            grid = [lst]
            rows = 1
            cols = len(lst)

        if rows == 1:
            row = grid[0]
            seen = defaultdict(list)
            unseen = defaultdict(deque)
            for c in range(cols):
                unseen[grid[0][c]].append((0,c))

            cnt = 0
            for c in range(cols):
                cnt += grid[0][c]
                seen[grid[0][c]].append((0,c))
                unseen[grid[0][c]].popleft()
                LEFT_HALF = cnt
                RIGHT_HALF = total_sum - LEFT_HALF
                diff = abs(LEFT_HALF - RIGHT_HALF)
                if LEFT_HALF == RIGHT_HALF:
                    return True 
                if LEFT_HALF > RIGHT_HALF:
                    if diff in seen:
                        if (0, 0) in seen[diff] or (0, c) in seen[diff]:
                            print("REACHEED")
                            return True 
                else:
                    if diff in unseen:
                        if (0, c+1) in unseen[diff] or (0, cols - 1) in unseen[diff]:
                            print("REACHEED")

                            return True
            return False
        for r in range(rows):
            for c in range(cols):
                bottom_mapping[grid[r][c]].append((r,c))

        cnt = 0
        for r in range(rows):
            for c in range(cols):
                cnt += grid[r][c]
                top_mapping[grid[r][c]].append((r,c))
                bottom_mapping[grid[r][c]].popleft()

            TOP_HALF = cnt
            BOTTOM_HALF = total_sum - cnt
            if TOP_HALF == BOTTOM_HALF: return True
            diff = abs(BOTTOM_HALF - TOP_HALF)
            if TOP_HALF > BOTTOM_HALF:
                # need remove diff from TOP HALF
                if diff in top_mapping:
                    # if r = 0 or r = rows - 2, its 1 dimensional so worry about remaining connected
                    if r == 0:
                        if (r, 0) in top_mapping[diff] or (r, cols - 1) in top_mapping[diff]:
                            return True
                    else:
                        return True
            else:
                # need remove diff from bottom half
                if diff in bottom_mapping:
                    # if r = 0 or r = rows - 2, its 1 dimensional so worry about remaining connected
                    if r == rows - 2:
                        if (r, 0) in bottom_mapping[diff] or (r, cols - 1) in bottom_mapping[diff]:
                            return True
                    else:
                        return True
        # VERTICAL CUTS
        left_mapping = defaultdict(list) # val : [idx1, idx2]
        right_mapping = defaultdict(deque) # val : [idx1, idx2]
        cnt = 0
        for c in range(cols):
            for r in range(rows):
                right_mapping[grid[r][c]].append((r,c))
        
        for c in range(cols):
            for r in range(rows):
                cnt += grid[r][c]
                left_mapping[grid[r][c]].append((r,c))
                right_mapping[grid[r][c]].popleft()
            LEFT_HALF = cnt
            RIGHT_HALF = total_sum - cnt
            if LEFT_HALF == RIGHT_HALF: return True
            diff = abs(LEFT_HALF - RIGHT_HALF)
            if LEFT_HALF > RIGHT_HALF:
                # need remove diff from LEFT HALF
                if diff in left_mapping:
                    if c == 0:
                        if (0, c) in left_mapping[diff] or (rows - 1, c) in left_mapping[diff]:
                            return True
                    else:
                        return True
            else:
                # need remove diff from RIGHT half
                if diff in right_mapping:
                    if c == 0 or c == cols - 2:
                        if (0, c + 1) in right_mapping[diff] or (rows - 1, c + 1) in right_mapping[diff]:
                            return True
                    else:
                        return True

        return False 

            

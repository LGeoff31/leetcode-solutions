class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # 1 8
        # 3 -2
        rows, cols = len(grid), len(grid[0])
        res = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]

        for r in range(rows - k + 1):
            for c in range(cols - k + 1):
                sorted_lst = []
                for dr in range(k):
                    for dc in range(k):
                        sorted_lst.append(grid[r + dr][c + dc])
                sorted_lst = list(set(sorted_lst)) # remove any dups
                if len(sorted_lst) == 1:
                    res[r][c] = 0
                    continue

                sorted_lst.sort()
                min_diff = float('inf')
                for i in range(1, len(sorted_lst)):
                    min_diff = min(min_diff, sorted_lst[i] - sorted_lst[i-1])
                res[r][c] = min_diff
        return res
                                # 729,000,000
            #         if abs(grid[new_r][new_c] - grid[new_r][new_c-1]) != 0:
            #             min_difference = min(min_difference, abs(grid[new_r][new_c] - grid[new_r][new_c-1]))
            #         if abs(grid[new_r][new_c] - grid[new_r-1][new_c]) != 0:
            #             min_difference = min(min_difference, abs(grid[new_r][new_c] - grid[new_r-1][new_c]))
            # print(min_difference)
            # # first row
            # for new_c in range(c+1, c+k): # 2
            #     min_difference = min(min_difference, abs(grid[r][new_c] - grid[r][new_c-1]))
            # # first col
            # for new_r in range(r+1, r+k):
            #     min_difference = min(min_difference, abs(grid[new_r][c] - grid[new_r-1][c]))
                    
        # 1 -2 3
        # 2 3 5
        # 39461 84541
        # -64975 33143

        
        # rows = 1
        # cols = 2

        # -88242,79613
        # -48040,69929


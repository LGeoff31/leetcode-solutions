class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        directions = [0, 1, 0, -1, 0] # four directions 
        
        @lru_cache(maxsize=None) # using python cache lib for memoization
        def dfs(r,c):
            ans=1                  
			# iterating through all 4 directions
            for i in range(4): 
                new_row,new_col=r+directions[i], c+directions[i+1] # calculating the new cell
				# check if new cell is within the grid bounds and is an increasing sequence
                if 0<=new_row<m and 0<=new_col<n and grid[new_row][new_col]>grid[r][c]: 
                    ans = max(ans, dfs(new_row, new_col) + 1 )  # finding the max length of valid path from the current cell                                      
            return ans
        
        return max(dfs(r,c) for r in range(m) for c in range(n)) 
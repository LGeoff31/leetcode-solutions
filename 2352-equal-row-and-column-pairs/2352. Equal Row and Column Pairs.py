class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row = []
        col = []

        for r in grid:
            string = ""
            for elem in r:
                string += str(elem) + " "
            row.append(string) 
        for i in range(len(grid)):
            string = ""
            for j in range(len(grid)):
                string += str(grid[j][i]) + " "
            col.append(string)
        count = 0
        print(row)
        print(col)
        for i in range(len(row)):
            for j in range(len(col)):
                if row[i] == col[j]: count += 1
        return count


#11, 1
#1, 11
                
        
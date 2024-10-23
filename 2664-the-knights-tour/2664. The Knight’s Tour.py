class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        rows, cols = m, n 

        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        self.res = []
        self.done = False
        def dfs(r,c, lst, counter):
            if self.done: return
            if counter == m*n:
                print('reached', lst)
                a = []
                for r in range(rows):
                    b = []
                    for c in range(cols):
                        b.append(lst[r*cols + c])
                    a.append(b)
                self.res = a
                self.done = True
                return
            
            for dr, dc in directions:
                if 0 <= r+dr < rows and 0 <= c+dc < cols and lst[cols * (r+dr) + (c+dc)] == -1:
                    lst[cols * (r+dr) + c+dc] = counter
                    dfs(r+dr, c+dc, lst, counter + 1)
                    lst[cols * (r+dr) + c+dc] = -1
                    

        lst = [-1] * cols * rows
        lst[r*cols + c] = 0
        dfs(r,c, lst, 1)
        return self.res
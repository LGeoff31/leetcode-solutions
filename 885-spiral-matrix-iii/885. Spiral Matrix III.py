class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # 1 -> 9 -> 25 -> 49 #(_, _) where _=(-2, -1, 0, 1, 2) -> 5x5 = 25, 5 + 5 + 4 + 4, 
        res = [(rStart, cStart)]
        i = 1
        right = True
        down = True
        a = 0
        while len(res) != rows*cols:
            a += 1
            for j in range(1): # Going right
                rStart = rStart
                cStart = cStart + 1
                if 0 <= cStart < cols and 0 <= rStart < rows and (rStart, cStart) not in res:
                    res.append((rStart, cStart))
            for j in range(i): # Going down
                rStart = rStart + 1
                cStart = cStart
                if 0 <= cStart< cols and 0 <= rStart < rows and (rStart, cStart) not in res:
                    res.append((rStart, cStart))
            for j in range(i+1): # Going left
                rStart = rStart
                cStart = cStart - 1
                if 0 <= cStart < cols and 0 <= rStart < rows and (rStart, cStart) not in res:
                    res.append((rStart, cStart))
            for j in range(i+1): # Going up
                rStart = rStart - 1
                cStart = cStart
                if 0 <= cStart < cols and 0 <= rStart < rows and (rStart, cStart) not in res:
                    res.append((rStart, cStart))
            for j in range(i+1):
                rStart = rStart
                cStart = cStart + 1
                if 0 <= cStart < cols and 0 <= rStart < rows and (rStart, cStart) not in res:
                    res.append((rStart, cStart))
            print(res)
            # if a == 2: break
            i += 2
            
        return res
        
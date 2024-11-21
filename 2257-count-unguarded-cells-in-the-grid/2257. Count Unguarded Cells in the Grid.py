class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        lst = [[0] * n for _ in range(m)]
        rows, cols = m, n
        visited = set()
        for r,c in walls:
            visited.add((r,c))
        for r,c in guards:
            visited.add((r,c))
        for r,c in guards:
            # print(lst)
            # Go right
            r1,c1 =r,c
            c1+=1
            while c1 < cols and (r1,c1) not in visited:
                lst[r1][c1] = 1
                c1 += 1
            # Go left
            r1,c1 =r,c
            c1-=1
            while c1 >= 0 and (r1,c1) not in visited:
                lst[r1][c1] = 1
                c1 -= 1
            # Go down
            r1,c1 =r,c
            r1 += 1
            while r1 < rows and (r1,c1) not in visited:
                lst[r1][c1] = 1
                r1 += 1
            # Go up
            r1,c1 =r,c
            r1-=1
            while r1 >= 0 and (r1,c1) not in visited:
                lst[r1][c1] = 1
                r1 -= 1
        print(lst)
        res = 0
        for r in range(rows):
            for c in range(cols):
                res += lst[r][c] == 1
        return n*m - res - len(walls) - len(guards)
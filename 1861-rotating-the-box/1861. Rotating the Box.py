class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        box = [[box[r][c] for r in range(rows)][::-1] for c in range(cols)]
        print(box)
        def drop(c):
            r = cols - 1
            while r >= 0:
                # basically go up until hit obstacle
                new_r = r
                gems = 0
                while r >= 0 and box[r][c] != "*":
                    if box[r][c] == "#":
                        box[r][c] = "."
                        gems += 1
                    r -= 1
                while new_r >= 0:
                    if gems > 0:
                        box[new_r][c] = "#"
                        gems -= 1
                    new_r -= 1
                r -= 1
                
        for c in range(rows):
            drop(c)
        return box

        return 
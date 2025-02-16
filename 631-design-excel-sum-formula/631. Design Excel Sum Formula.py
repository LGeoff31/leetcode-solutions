class Excel:
    def __init__(self, height: int, width: str):
        width = ord(width) - ord("A") + 1
        self.spreadsheet = [[0] * width for _ in range(height)]
        print(self.spreadsheet)

    def set(self, row: int, column: str, val: int) -> None: #O(1)
        r,c = row - 1, ord(column) - ord("A")
        self.spreadsheet[r][c] = val
        print(self.spreadsheet)

    def get(self, row: int, column: str) -> int: #O(1) 
        r,c = row - 1, ord(column) - ord("A")
        return self.evaluate(r, c)

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        r,c = row - 1, ord(column) - ord("A")
        self.spreadsheet[r][c] = numbers
        return self.evaluate(r,c)

    def evaluate(self, r, c):
        if type(self.spreadsheet[r][c]) == int:
            return self.spreadsheet[r][c]
        # Otherwise, form: ["A1", "A1:B2"]
        res = 0
        for expr in self.spreadsheet[r][c]:
            if ":" not in expr:
                nxt_r, nxt_c = int(expr[1:]) - 1, ord(expr[0]) - ord("A")
                res += self.evaluate(nxt_r, nxt_c)
            else:
                start_coord, end_coord = expr.split(":")
                start_r, start_c = int(start_coord[1:]) - 1, ord(start_coord[0]) - ord("A") 
                end_r, end_c = int(end_coord[1:]) - 1, ord(end_coord[0]) - ord("A") 
                for r_pos in range(start_r, end_r + 1):
                    for c_pos in range(start_c, end_c + 1):
                        res += self.evaluate(r_pos, c_pos)
        return res
      

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.spreadsheet = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        r,c = int(cell[1:]) - 1, ord(cell[0]) - ord("A")
        self.spreadsheet[r][c] = value

    def resetCell(self, cell: str) -> None:
        r,c = int(cell[1:]) - 1, ord(cell[0]) - ord("A")
        self.spreadsheet[r][c] = 0

    def getValue(self, formula: str) -> int:
        print('formula', formula)
        operands = formula[1:].split("+")
        print(operands, formula)
        x,y = operands[0], operands[1]
        return self.evaluate(x) + self.evaluate(y)

    def evaluate(self, val):
        print('val', val, val[0], val[0].isdigit(), type(val[0]), len(val[0]))
        if val[0].isdigit() or val[0] == 0:
            return int(val)
        print('nigg', val[0], val[0] == "0")
        r,c = int(val[1:]) - 1, ord(val[0]) - ord("A")
        return self.spreadsheet[r][c]


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
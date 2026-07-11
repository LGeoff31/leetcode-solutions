class Spreadsheet:
    def __init__(self, rows: int):
        self.cells = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        a,b = formula[1:].split("+")
        if a.isnumeric():
            a = int(a)
        else:
            a = self.cells[a]
        if b.isnumeric():
            b = int(b)
        else:
            b = self.cells[b]
        
        return a+b


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
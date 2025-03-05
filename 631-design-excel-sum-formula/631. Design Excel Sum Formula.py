class Excel:
    def __init__(self, height: int, width: str):
        self.spreadsheet = {} # {(r,c) : value}
    
    def set(self, row: int, column: str, val: int) -> None:
        self.spreadsheet[column + str(row)] = val

    def get(self, row: int, column: str) -> int: 
        return self.evaluate(column + str(row))

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        res = 0
        self.spreadsheet[column + str(row)] = numbers
        for expr in numbers:
            res += self.evaluate(expr)
        print(self.spreadsheet, res)
        return res
    
    def evaluate(self, expr):
        if expr in self.spreadsheet and type(self.spreadsheet[expr]) == int:
            return self.spreadsheet[expr]
        if expr in self.spreadsheet and type(self.spreadsheet[expr]) == list:
            print('reached')
            res = 0
            for e in self.spreadsheet[expr]:
                res += self.evaluate(e)
            return res
        if ":" not in expr:
            column, row = expr[0], expr[1:]
            if (column + str(row)) not in self.spreadsheet: return 0
            return self.evaluate(column + str(row))
        else:
            res = 0
            lhs, rhs = expr.split(":")
            r1, c1 = int(lhs[1:]), lhs[0]
            r2, c2 = int(rhs[1:]), rhs[0]
            for r in range(r1, r2+1):
                for c in range(ord(c1), ord(c2) + 1):
                    if (chr(c) + str(r)) in self.spreadsheet:
                        res += self.evaluate(chr(c) + str(r))
            return res

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
class Excel:
    """
    [
        ["1"], ["0"], ["0"]
        ["0"], ["0"], ["0"]
        ["0"], ["0"], ["0"]
        ["0"], ["0"], ["0"]
        ["0"], ["0"], ["0"]
        ["0"], ["0"], ["0"]
        ["0"], ["0"], ["0"]
        ["0"], ["0"], ["0"]
        ["0"], ["0"], ["0"]
        ["1"], ["0"], ["0"], ["0], 

    ]
    """
    def __init__(self, height: int, width: str):
        self.rows = height
        self.cols = ord(width) - ord("A") + 1
        # Each cell contains either ["0"] or expression ["A3:B4", "A1:B2"]
        self.grid = [[0] * self.cols for _ in range(self.rows)]
        
    def set(self, row: int, column: str, val: int) -> None: 
       self.grid[row-1][ord(column)-ord("A")] = val

    def get(self, row: int, column: str) -> int: #O(1)
        v = self.grid[row - 1][ord(column) - ord("A")]
        if type(v) == int:
            return int(v)
        return self.evaluate(v)

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        self.grid[row-1][ord(column)-ord("A")] = numbers
        val = self.evaluate(numbers)
        return val

    def evaluate(self, expr):
        res = 0
        if type(expr) == int:
            return expr
        for e in expr:
            if ":" in e: 
                start, end = e.split(":") 
                for r in range(int(start[1:]) - 1, int(end[1:])): 
                    for c in range(ord(start[0])-ord("A"), ord(end[0])-ord("A") + 1):
                        res += self.evaluate(self.grid[r][c])
            elif type(e) == int:
                res += e
            else:
                res += self.evaluate(self.grid[int(e[1]) - 1][ord(e[0])-ord("A")])
        return res

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
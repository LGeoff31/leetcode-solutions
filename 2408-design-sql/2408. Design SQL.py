class SQL:
    """
    ["SQL","ins","sel","ins","exp","rmv","sel","exp"]
    [[["one","two","three"],[2,3,1]],["two",["first","second","third"]],["two",1,3],["two",["fourth","fifth","sixth"]],["two"],["two",1],["two",2,2],["two"]]

    Output: [null,true,"third",true,["1,first,second,third","2,fourth,fifth,sixth"],null,"fifth",["2,fourth,fifth,sixth"]]
    """

    def __init__(self, names: List[str], columns: List[int]):
        self.n = len(names)
        self.tables = {}
        self.rowIds = {}
        self.colsMap = {}
        for i, name in enumerate(names):
            self.rowIds[name] = 1
            self.colsMap[name] = columns[i]
            self.tables[name] = {}

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.colsMap or len(row) != self.colsMap[name] or name not in self.tables: return False
        self.tables[name][self.rowIds[name]] = row
        self.rowIds[name] += 1
        return True
        
    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.tables or rowId not in self.tables[name].keys(): return
        del self.tables[name][rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables or rowId not in self.tables[name]: return "<null>"
        for i in range(len(self.tables[name][rowId])):
            if i+1 == columnId:
                return self.tables[name][rowId][i]
        return "<null>"

    def exp(self, name: str) -> List[str]:
        if name not in self.tables: return []
        output = []
        # count = 1
        for key in self.tables[name]:
            string = ""
            for attribute in self.tables[name][key]:
                string += attribute + ","
            string = string[:-1]
            output.append(str(key) + "," + string)
            # count += 1
        return output


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)
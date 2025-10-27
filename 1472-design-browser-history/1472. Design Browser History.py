class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        while len(self.arr) != self.idx+1:
            self.arr.pop()
        self.idx += 1
        self.arr.append(url)
        

    def back(self, steps: int) -> str:
        print(self.idx, self.arr)
        self.idx = max(0, self.idx - steps)
        return self.arr[self.idx]


    def forward(self, steps: int) -> str:
        self.idx = min(len(self.arr) - 1, self.idx + steps)
        return self.arr[self.idx]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
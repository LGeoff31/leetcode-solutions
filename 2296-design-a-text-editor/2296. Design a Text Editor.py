class TextEditor:
    def __init__(self):
        self.string = ""
        self.cursor = 0

    def addText(self, text: str) -> None:
        self.string = self.string[: self.cursor] + text + self.string[self.cursor: ]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        if self.cursor < k:
            # You don't delete k characters, meaning the cursor < k
            self.string = self.string[self.cursor:]
            tmp = self.cursor
            self.cursor = 0
            return tmp
        else:
            cutoff_idx = self.cursor - k
            self.string = self.string[: cutoff_idx] + self.string[self.cursor:]
            self.cursor -= k
            return k

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)
        res = self.string[: self.cursor]
        if len(res) > 10:
            return res[len(res) - 10 : ]
        return res

    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.string), k + self.cursor)
        res = self.string[:self.cursor]
        if len(res) > 10:
            return res[len(res) - 10 : ]
        return res

        
#practice

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)


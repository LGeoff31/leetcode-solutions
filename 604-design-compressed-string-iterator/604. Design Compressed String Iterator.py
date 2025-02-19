class StringIterator:
    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.lst = []
        self.i = 0
        self.counter = 0
        self.string = ""

    def next(self) -> str:
        if self.i >= len(self.compressedString) and self.counter == 0:
            return " "
        if self.counter == 0:
            string = ""
            while self.i < len(self.compressedString) and not self.compressedString[self.i].isdigit():
                string += self.compressedString[self.i]
                self.i += 1
            self.string = string
            # Get the number
            number = ""
            while self.i < len(self.compressedString) and self.compressedString[self.i].isdigit():
                number += self.compressedString[self.i]
                self.i += 1
            self.counter = int(number)
            print(self.counter, self.string)
        self.counter -= 1
        return self.string

    def hasNext(self) -> bool:
        print(self.counter, self.i)
        if self.i == len(self.compressedString) and self.counter == 0:
            return False
        return True

        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
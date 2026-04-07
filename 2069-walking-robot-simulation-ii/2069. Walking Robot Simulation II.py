class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.directions = ["E", "N", "W", "S"]
        self.idx = 0
        self.x, self.y = 0, 0
        self.perimeter = 2*width + 2*height - 4

    def step(self, num: int) -> None:
        if num > 0:
            num %= self.perimeter
            if num == 0:
                num = self.perimeter

        while num > 0:
            d = self.directions[self.idx]
            if d == "E":
                diff = self.width - self.x - 1
                if num >= diff:
                    self.x = self.width - 1
                    if num > diff:
                        self.idx = (self.idx + 1) % 4
                    num -= diff
                else:
                    self.x += num
                    num = 0
            elif d == "N":
                diff = self.height - self.y - 1
                if num >= diff:
                    self.y = self.height - 1
                    if num > diff:
                        self.idx = (self.idx + 1) % 4
                    num -= diff
                else:
                    self.y += num
                    num = 0
            elif d == "W":
                diff = self.x
                if num >= diff:
                    self.x = 0
                    if num > diff:
                        self.idx = (self.idx + 1) % 4
                    num -= diff
                else:
                    self.x -= num
                    num = 0
            elif d == "S":
                diff = self.y
                if num >= diff:
                    self.y = 0
                    if num > diff:
                        self.idx = (self.idx + 1) % 4
                    num -= diff
                else:
                    self.y -= num
                    num = 0

    def getPos(self) -> List[int]:
        return [self.x, self.y]        

    def getDir(self) -> str:
       d= self.directions[self.idx]
       if d == "E": return "East"
       if d == "W": return "West"
       if d == "N": return "North"
       if d == "S": return "South"



# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
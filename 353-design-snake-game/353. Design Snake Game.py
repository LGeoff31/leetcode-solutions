class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.r = 0
        self.c = 0
        self.food = food
        self.score = 0
        self.idx = 0
        self.queue = deque([(0,0)])

    def update_coordinate(self, direction):
        match direction:
            case "R":
                self.c += 1
            case "L":
                self.c -= 1
            case "U":
                self.r -= 1
            case default:
                self.r += 1
        return [self.r, self.c]
    def inBounds(self, r,c):
        return 0 <= r < self.height and 0 <= c < self.width

    def hitSnake(self):
        return (self.r, self.c) in self.queue

    def move(self, direction: str) -> int:
        self.r, self.c = self.update_coordinate(direction)
        if not self.inBounds(self.r, self.c):
            return -1
        print(self.queue, self.r, self.c)
        if self.idx >= len(self.food):
            self.queue.popleft()
            if self.hitSnake():
                return -1
            self.queue.append((self.r,self.c))
            return self.score
        if [self.r, self.c] == self.food[self.idx]:
            self.idx += 1
            self.score += 1
        else:
            self.queue.popleft()
        if self.hitSnake():
            return -1
        self.queue.append((self.r,self.c))
        return self.score
        
        



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
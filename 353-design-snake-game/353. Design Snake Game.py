class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.rows, self.cols = height, width
        self.occupied_cells = set([(0,0)])
        self.queue = deque([(0,0)])
        self.food = food
        self.food_idx = 0

    def get_new_position(self, direction, old_r, old_c):
        delta_c, delta_r = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}[direction]
        return old_r + delta_r, old_c + delta_c

    def move(self, direction: str) -> int:
        old_r, old_c = self.queue[-1]
        r,c = self.get_new_position(direction, old_r, old_c)
        food_r, food_c = self.food[self.food_idx] if self.food_idx < len(self.food) else [-1, -1]
        # Out of bounds
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return -1
        
        if not(r == food_r and c == food_c):
            gone_r, gone_c = self.queue.popleft()
            self.occupied_cells.remove((gone_r, gone_c))
        else:
            self.food_idx += 1

        # Collision with tail
        if (r,c) in self.occupied_cells:
            return -1
        

        self.queue.append((r,c))
        self.occupied_cells.add((r,c))
        print(self.queue)

        return len(self.occupied_cells) -1
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
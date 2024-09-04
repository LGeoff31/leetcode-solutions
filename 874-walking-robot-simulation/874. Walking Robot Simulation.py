class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0  # Starts facing North
        
        # Set of obstacles for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        x, y = 0, 0
        max_distance_sq = 0
        
        for command in commands:
            if command == -2:  # Turn left
                direction = (direction - 1) % 4
            elif command == -1:  # Turn right
                direction = (direction + 1) % 4
            else:  # Move forward
                for _ in range(command):
                    next_x = x + directions[direction][0]
                    next_y = y + directions[direction][1]
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        max_distance_sq = max(max_distance_sq, x * x + y * y)
                    else:
                        break
        
        return max_distance_sq

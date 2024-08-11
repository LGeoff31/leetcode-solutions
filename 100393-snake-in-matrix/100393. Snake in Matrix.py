class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        res = 0
        for command in commands:
            if command == 'RIGHT':
                res += 1
            elif command == "LEFT":
                res -= 1
            elif command == "DOWN":
                res += n
            else:
                res -= n
        return res

        
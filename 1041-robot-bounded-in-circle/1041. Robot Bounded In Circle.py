class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0, 0
        idx = 0
        def new_spot(x,y):
            match idx:
                case 0:
                    y += 1
                case 1:
                    x += 1
                case 2:
                    y -= 1
                case 3:
                    x -= 1
            return x,y

        for i in range(4):
            for c in instructions:
                if c == "G":
                    x,y = new_spot(x,y)
                elif c == "L":
                    idx = (idx-1) % 4
                else:
                    idx = (idx+1) % 4
            if x == 0 and y == 0:
                return True
        return False


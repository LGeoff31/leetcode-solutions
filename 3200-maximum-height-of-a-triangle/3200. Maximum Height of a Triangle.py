class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def calc(blue_turn, red, blue, bc, rc):
            count = 0
            while True:
                if blue_turn:
                    if blue - bc >= 0:
                        blue-=bc
                        bc+=2
                        # print("blue", blue)
                        count += 1
                    else:
                        break
                else:
                    if red - rc >= 0:
                        red -= rc
                        rc += 2
                        count += 1
                    else:
                        break
                blue_turn = not blue_turn
            return count
        print(calc(False, red, blue, 1, 2))
        return max(calc(True, red, blue, 1, 2), calc(False, red,blue,2,1))
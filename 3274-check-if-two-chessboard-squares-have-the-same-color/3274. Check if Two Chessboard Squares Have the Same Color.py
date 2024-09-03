class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def find_color(coordiante): # True -> White
            letter, number = coordiante[0], coordiante[1]
            number = int(number)
            if letter in "aceg":
                return number % 2 == 0
            else:
                return number % 2 == 1
        return find_color(coordinate1) == find_color(coordinate2)
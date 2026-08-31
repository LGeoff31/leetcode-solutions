class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        """
        row+col % 2:
        - 1: black
        - 0: white

        we can instantly tell if source % 2 != target % 2

        otherwise, the answer should always be either 1 or 2

        1 -> same diagonal
        2 -> different digonal
        """
        if sum(source) % 2 != sum(target) % 2:
            return -1
        
        if sum(source) == sum(target) or target[0] - source[0] == target[1] - source[1]:
            return 1
        return 2
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r, l = moves.count("R"), moves.count("L")
        if r < l:
            return l-r + moves.count("_")
        else:
            return r-l + moves.count("_")
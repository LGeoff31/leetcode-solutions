class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        total_distance = 0

        for r, c in nuts:
            manhattan = abs(tree[0] - r) + abs(tree[1] - c)
            total_distance += manhattan
        min_distance = float('inf')
        for r, c in nuts:
            distance_to_squirrel = abs(squirrel[0] - r) + abs(squirrel[1] - c)
            manhattan = abs(tree[0] - r) + abs(tree[1] - c)
            trip_distance = (total_distance * 2) - manhattan + distance_to_squirrel
            min_distance = min(min_distance, trip_distance)

        return min_distance 
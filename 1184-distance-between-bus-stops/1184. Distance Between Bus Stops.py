class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            return min(sum(distance[start:]) + sum(distance[:destination]), sum(distance) - (sum(distance[start:]) + sum(distance[:destination])))
        return min(sum(distance[start:destination]), sum(distance)-sum(distance[start:destination]))
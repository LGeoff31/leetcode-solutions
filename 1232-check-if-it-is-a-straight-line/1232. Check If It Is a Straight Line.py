class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()

        def get_slope(coord1, coord2):
            if coord1[0]-coord2[0] == 0:
                return 1e9
            return (coord1[1] - coord2[1]) / (coord1[0] - coord2[0])

        slope = get_slope(coordinates[1], coordinates[0])
        print(slope)
        for i in range(2, len(coordinates)):
            if get_slope(coordinates[i], coordinates[i-1]) != slope:
                return False 
        return True
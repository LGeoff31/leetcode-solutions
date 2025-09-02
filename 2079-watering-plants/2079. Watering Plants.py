class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        curr = capacity
        for i in range(len(plants)):
            if curr < plants[i]:
                res += 2*(i+1) - 1
                curr = capacity - plants[i]
            else:
                res += 1
                curr -= plants[i]
            print(res)
        return res
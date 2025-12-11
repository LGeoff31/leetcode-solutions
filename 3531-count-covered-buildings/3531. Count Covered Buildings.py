class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        vert = defaultdict(list)
        horz = defaultdict(list)

        for x,y in buildings:
            horz[x].append(y)
            vert[y].append(x)
        for key in vert:
            vert[key].sort()
        for key in horz:
            horz[key].sort()
        res = 0
        print(vert)
        print(horz)
        for x,y in buildings:
            if len(horz[x]) >= 3 and y != horz[x][0] and y != horz[x][-1] and len(vert[y]) >= 3 and x != vert[y][0] and x != vert[y][-1]:
                res += 1
        return res
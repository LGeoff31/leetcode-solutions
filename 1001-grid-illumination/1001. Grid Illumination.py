class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row, col, diagS, diagP = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        mySet = set()
        for i in range(len(lamps)):
            if (lamps[i][0], lamps[i][1]) not in mySet:
                row[lamps[i][0]] = 1 + row.get(lamps[i][0], 0)
                col[lamps[i][1]] = 1 + col.get(lamps[i][1], 0)
                diagS[sum(lamps[i])] = 1 + diagS.get(sum(lamps[i]), 0)
                diagP[lamps[i][0] - lamps[i][1]] = 1 + diagP.get(lamps[i][0] - lamps[i][1], 0)
                mySet.add((lamps[i][0], lamps[i][1]))
        ans = []
        directions = [(-1, -1), (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0), (1, 1), (1, -1), (-1, 1)]
        def check(r, c):
            if (r in row and row[r] > 0) or (c in col and col[c] > 0) or (r+c in diagS and diagS[r+c] > 0) or (r-c in diagP and diagP[r-c] > 0):
                return True
            return False
        for i in range(len(queries)):
            if check(queries[i][0], queries[i][1]):
                ans.append(1)
                #remove all lamps within 3x3
                for dr,dc in directions:
                    if (queries[i][0] + dr, queries[i][1] + dc) in mySet:
                        lamp_r, lamp_c = queries[i][0] + dr, queries[i][1] + dc
                        row[lamp_r] -= 1
                        col[lamp_c] -= 1
                        diagS[lamp_r + lamp_c] -= 1
                        diagP[lamp_r - lamp_c] -= 1
                        mySet.remove((lamp_r, lamp_c))
            else:
                ans.append(0)
        return ans
        
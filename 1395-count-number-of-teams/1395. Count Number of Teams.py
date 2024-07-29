class Solution:
    def numTeams(self, rating: List[int]) -> int:
        increasing = defaultdict(list)
        decreasing = defaultdict(list)

        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    increasing[i].append(j)
                else:
                    decreasing[i].append(j)
        res = 0
        for i in range(len(rating)):
            # Check 2 steps in increasing way
            for nei in increasing[i]:
                res += len(increasing[nei])

            # Check 2 steps in decreasing way
            for nei in decreasing[i]:
                res += len(decreasing[nei])
        return res
        # Interesting follow up for n soilders -> BFS??



        
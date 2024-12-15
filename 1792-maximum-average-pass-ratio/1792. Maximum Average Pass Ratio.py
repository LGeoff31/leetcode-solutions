class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # What would increase the sum the most?
        # Pick a option that has small denominator and ensure it's not of form x/x
        # If there's a tie, pick the one with the smaller denomintator


        lst = []
        for a,b in classes:
            profit = (a+1)/(b+1) - a/b
            heappush(lst, (-profit, a, b))
        
        for i in range(extraStudents):
            profit, a, b = heappop(lst)
            new_profit = (a+2)/(b+2) - (a+1)/(b+1)
            heappush(lst, (-new_profit,a+1,b+1))
        print(lst)
        res = 0
        for a,b,c in lst:
            res += b/c
        return res / len(lst)

        # 4/6 - 3/5 = 0.0666666667
        # 5/6 - 4/5 = 0.0333333333

        # 5/6 - 4/5 = 0.03333
        # 5/7 - 4/6 = 0.0476190476
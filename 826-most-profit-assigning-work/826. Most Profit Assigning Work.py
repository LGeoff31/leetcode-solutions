class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        lst = sorted([[x,y] for x,y in zip(difficulty, profit)])
        prevMaxProfit = lst[0][1]
        difficulty.sort()
        for i in range(1, len(difficulty)):
            lst[i][1] = max(lst[i][1], prevMaxProfit)
            prevMaxProfit = max(prevMaxProfit, lst[i][1])



        res = 0
        print(lst, difficulty)
        for w in worker:
            highest_idx = bisect.bisect_left(difficulty, w+0.000001) - 1
            print(highest_idx)
            res += lst[highest_idx][1] if highest_idx >= 0 else 0
            print(res)

        return res
        
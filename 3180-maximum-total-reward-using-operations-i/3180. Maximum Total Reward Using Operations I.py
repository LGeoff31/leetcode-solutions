class Solution:
    def maxTotalReward(self, lst: List[int]) -> int:
        lst.sort()
        dp = set()
        dp.add(0)
        dp.add(lst[0])
        for i in range(1, len(lst)):
            newDP = set()
            for element in dp:
                if lst[i] > element:
                    newDP.add(element + lst[i])
                newDP.add(element)
            dp = newDP
        return max(dp)
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        # DP?? O(n^2)
        # dp[i][j] = min time to complete the ith potion in time j
        # return min(dp[-1])
        n, m = len(skill), len(mana)
        lst = [0]
        for wizard in range(n):
            lst.append(lst[-1] + (mana[0] * skill[wizard])) # THis has 
        print(lst) # THis has m+1 elements so this is good
        for potion in range(1, m): # 0 -> 3
            x = 0
            incrementer = 0
            for wizard in range(n): # 0 -> 3
                x = max(x, lst[wizard+1] - (incrementer))
                incrementer += skill[wizard] * mana[potion]
            lst = [x]
            for wizard in range(n):
                lst.append(lst[-1] + (mana[potion] * skill[wizard]))
            print(x)
        print(lst)
        return lst[-1]
                
                
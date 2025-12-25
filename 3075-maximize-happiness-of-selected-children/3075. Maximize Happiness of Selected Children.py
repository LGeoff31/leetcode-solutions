class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        happiness.sort()
        dic = Counter(happiness)
        cnt = len(happiness) - 1
        x = 1
        for i in range(len(happiness) -1, -1, -1):
            res += max(0, happiness[i] - (x-1))
            k -= 1
            
            cnt -= 1
            if x in dic and k:
                cnt -= dic[x]
            x+=1
            if k == 0: break
            print(res)
        print(res)
        return res
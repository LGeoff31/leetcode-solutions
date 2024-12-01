class Solution:
    def getHint(self, secret: str, guess: str) -> str:  
        res1, res2 = 0, 0
        a,b = Counter(secret), Counter(guess)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                res1 += 1
        dic = {}
        for key in a:
            if key in b:
                dic[key] = min(a[key], b[key])
        nonoverlapping = 0
        for key in dic:
            nonoverlapping += dic[key]
        return str(res1) + "A" + str(nonoverlapping - res1) + "B"
        
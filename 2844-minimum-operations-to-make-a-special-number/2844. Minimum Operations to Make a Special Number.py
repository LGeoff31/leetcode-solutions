class Solution:
    def minimumOperations(self, num: str) -> int:
        #-> 00, 25, 50, 75, or len()==1 and its 0

        res = 1e9
        n = len(num)
        possible = [(0,0), (2,5), (5,0), (7,5)]
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                for a,b in possible:
                    if num[i] == str(a) and num[j] == str(b):
                        res = min(res, j-i-1+n-j-1)
        return min(res, len(num)-num.count("0"))

        
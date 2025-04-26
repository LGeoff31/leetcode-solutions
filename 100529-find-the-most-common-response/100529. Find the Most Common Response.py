class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        dic = defaultdict(int)
        for arr in responses:
            for key in set(arr):
                dic[key] += 1
        maxVal = max(dic.values()) 
        res = "z" * 1003
        print(maxVal)
        print(dic)
        for key in dic:
            if dic[key] == maxVal and key < res:
                res = key
                # res = min(res, key)
        return res
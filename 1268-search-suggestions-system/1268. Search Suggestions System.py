class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l, r = 0, len(products)-1
        idx = 0
        res = []
        
        for i in range(len(searchWord)):
            c = searchWord[i]

            while l<=r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            
            while l<=r and (len(products[r]) <= i or products[r][i] != c):
                r-=1
            
            remain = r - l + 1
            res.append([])
            for j in range(min(remain, 3)):
                res[-1].append(products[j+l])
        return res


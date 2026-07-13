class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        min_length, max_length = min(len(a) for a in products), max(len(a) for a in products)
        curr = ""
        print(min_length, max_length)
        for i in range(len(searchWord)):
            curr += searchWord[i]
            leftIdx = bisect_left(products, curr)
            rightIdx = bisect_right(products, curr + 'z' * 1000)
            print(leftIdx, rightIdx)
            lst = [products[i] for i in range(leftIdx, min(rightIdx, len(products)))]
            lst = sorted(lst)[:3]
            res.append(lst)

        return res
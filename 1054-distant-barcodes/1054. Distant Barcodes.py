class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        dic = Counter(barcodes)
        maxHeap = []
        for key in dic:
            heappush(maxHeap, (-dic[key], key))
        res = []
        print(maxHeap)
        while maxHeap:
            # Take highest freq
            f1, n1 = heappop(maxHeap)
            print(f1, n1)
            f1 = -f1
            # Take second highest freq
            f2, n2 = -1, -1
            if maxHeap:
                f2, n2 = heappop(maxHeap)
                f2 = -f2
            res.append(n1)
            if f1-1 > 0:
                heappush(maxHeap, (-(f1-1), n1))
            if f2 != -1:
                res.append(n2)
                if f2-1 > 0:
                    heappush(maxHeap, (-(f2-1), n2))
            
        return res
            
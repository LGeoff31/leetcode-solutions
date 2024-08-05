class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a = Counter(arr)
        seen = set()
        j = 0
        for l in arr:
            if l not in seen and a[l] == 1:
                j += 1
                if k == j:
                    return l
        return ""

            
        
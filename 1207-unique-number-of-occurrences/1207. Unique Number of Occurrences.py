from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = Counter(arr)
        visited = set()
        for key in a:
            if a[key] in visited:
                return False
            visited.add(a[key])
        return True 
        
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(arr)
        rank = 1
        if not arr: return []
        dist = {a[0]: 1}
        prev = a[0]
        for i in range(1, len(a)):
            if a[i] != prev:
                rank += 1
                dist[a[i]] = rank
                prev = a[i]
        if a[-1] not in dist:
            dist[a[-1]] = rank+1
        return [dist[n] for n in arr]
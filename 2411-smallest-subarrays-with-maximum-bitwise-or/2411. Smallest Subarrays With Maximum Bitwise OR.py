class Solution:
    def smallestSubarrays(self, a: List[int]) -> List[int]:
        return [*map(lambda d:max(d.values())-d[-1]+1,accumulate(range(len(a)-1,-1,-1),
            lambda d,i:d|{q:i for q in range(32) if a[i]&1<<q}|{-1:i},initial={-1:0}))][:0:-1]
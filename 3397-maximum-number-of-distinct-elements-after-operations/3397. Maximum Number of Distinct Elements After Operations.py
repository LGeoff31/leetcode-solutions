class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        seen = set()
        res = 0
        nums.sort()
        max_elem = -1e9
        for n in nums:
            for i in range(max(-k, max_elem-n), k+1):
                if n+i not in seen:
                    max_elem = n+i
                    seen.add(n+i)
                    break
        return len(seen)

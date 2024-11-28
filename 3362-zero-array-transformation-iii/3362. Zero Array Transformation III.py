class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        q = deque(sorted(queries))
        a = []
        w = []

        for i in range(len(nums)):
            while q and q[0][0] <= i:
                heappush(a, -q.popleft()[1])
            while w and w[0] < i:
                heappop(w)
            while nums[i] > len(w):
                if a and -a[0] >= i:
                    heappush(w, -heappop(a))
                else:
                    return -1
        return len(a)

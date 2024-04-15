class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m,n = len(nums1), len(nums2)
        res = []

        h = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()
        visited.add((0,0))
        while k and h:
            val, i, j = heapq.heappop(h)
            res.append((nums1[i], nums2[j]))

            if i + 1 < m and (i+1, j) not in visited:
                visited.add((i+1, j))
                heapq.heappush(h, (nums1[i+1] + nums2[j], i+1, j))
            if j + 1 < n and (i, j+1) not in visited:
                visited.add((i, j+1))
                heapq.heappush(h, (nums1[i] + nums2[j+1], i, j+1))
            k -= 1
        return res

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        banned_set = set(banned)
        res = [-1] * n
        res[p] = 0
        queue = deque([p])
        steps = 1
        visited = set()
        visited.add(p)
        buckets = [SortedList(), SortedList()]
        for i in range(n):
            if i != p and i not in banned_set:
                buckets[i&1].add(i)
        print(buckets)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                left, right = max(node-k+1,0), min(node+k-1, n-1) - (k-1)
                left = 2 * left + k - 1 - node
                right = 2 * right + k - 1 - node
                elements_query = []

                for i in list(buckets[left%2].irange(left, right)):
                    if i in banned_set or i not in buckets[i % 2]:
                        continue
                    if i not in visited:
                        visited.add(i)
                        res[i] = steps
                        queue.append(i)
                        buckets[i%2].remove(i)
            steps += 1

        return res
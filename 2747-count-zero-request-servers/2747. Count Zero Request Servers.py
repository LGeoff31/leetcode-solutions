class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        """
        [1, 4], is it in [1,3]

        [2,4]

        """
        new_to_old = {}

        queries_with_idx = []
        for i, val in enumerate(queries):
            queries_with_idx.append((val, i))
        
        queries_with_idx.sort()

        for new_idx, (val, old_idx) in enumerate(queries_with_idx):
            new_to_old[new_idx] = old_idx
        
        queries.sort()
        logs.sort(key=lambda x:x[1])
        res = [None] * len(queries)
        start = queries[0] - x

        l = bisect_left(logs, start, key=lambda x:x[1])
        r = l
        unique_servers = defaultdict(int)

        print(logs, l, r)
        for new_idx, query in enumerate(queries):
            start, end = query - x, query

            # SHRINK WINDOW
            while l < len(logs) and logs[l][1] < start:
                if logs[l][0] in unique_servers:
                    unique_servers[logs[l][0]] -= 1
                    if unique_servers[logs[l][0]] == 0:
                        del unique_servers[logs[l][0]]
                l += 1
            # EXPAND WINDOW

            while r < len(logs) and logs[r][1] < start:
                r += 1

            while r < len(logs) and logs[r][1] <= end:
                unique_servers[logs[r][0]] += 1
                r += 1

            # print(unique_servers, l, r, start, end)
            res[new_to_old[new_idx]] = (n - len(unique_servers))

        return res






        
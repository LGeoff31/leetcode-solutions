class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        """
        1 2 3
        0 2 3 
        0 2 3

        """
        res = 0
        c, r = set(), set()
        c_count, r_count = 0, 0
        c_sum, r_sum = 0, 0
        queries = queries[::-1]
        print(queries)
        for t, index, value in queries:
            if t == 0:
                if index in r:
                    continue
                r.add(index)
                r_count += 1
                r_sum += value
                res += (n-c_count)*value # 20 want 18
            else:
                if index in c:
                    continue
                c.add(index)
                c_count += 1
                c_sum += value
                res += (n-r_count)*value
            print(res, c_count, c_sum, r_count, r_sum)
        return res


        # res = 12
        # res = 
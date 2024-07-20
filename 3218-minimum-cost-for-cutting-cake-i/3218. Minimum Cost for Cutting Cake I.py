class Solution:
    def minimumCost(self, m: int, n: int, h_lst: List[int], v_lst: List[int]) -> int:
        h_lst.sort(reverse=True)
        v_lst.sort(reverse=True)
        res = 0
        h, v = 0, 0
        h_len, v_len = len(h_lst), len(v_lst)
        h_count, v_count = 1, 1

        while h < h_len and v < v_len:
            if h_lst[h] >= v_lst[v]:
                res += h_lst[h] * v_count
                h += 1
                h_count += 1
            else:
                res += v_lst[v] * h_count
                v += 1
                v_count += 1
        
        while h < h_len:
            res += h_lst[h] * v_count
            h += 1
            h_count += 1
        while v < v_len:
            res += v_lst[v] * h_count
            v += 1
            v_count += 1
        return res


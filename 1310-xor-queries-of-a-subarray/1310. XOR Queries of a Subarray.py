class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = []
        a = 0
        for i in range(len(arr)):
            a ^= arr[i]
            prefix.append(a)
        res = []
        for start, end in queries:
            if start == 0:
                res.append(prefix[end])
            else:
                res.append(prefix[end] ^ prefix[start - 1])
        return res
        
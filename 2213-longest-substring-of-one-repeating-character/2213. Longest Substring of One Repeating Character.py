class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        s, n = list(s), len(s)
        runs = [len(list(g)) for _, g in groupby(s)]
        starts = SortedList(accumulate(runs, initial=0))  # boundary positions + sentinel n
        lens = SortedList(runs)  # multiset of gap lengths

        def add_break(p):
            j = starts.bisect_left(p)
            l, r = starts[j - 1], starts[j]
            starts.add(p)
            lens.remove(r - l)
            lens.add(p - l)
            lens.add(r - p)

        def remove_break(p):
            j = starts.bisect_left(p)
            l, r = starts[j - 1], starts[j + 1]
            starts.pop(j)
            lens.remove(p - l)
            lens.remove(r - p)
            lens.add(r - l)

        result = []
        for i, c in zip(queryIndices, queryCharacters):
            if c != (old := s[i]):
                for p, nb in ((i, i - 1), (i + 1, i + 1)):
                    if 0 <= nb < n:
                        if s[nb] == old: add_break(p)
                        elif s[nb] == c: remove_break(p)
                s[i] = c
            result.append(lens[-1])

        return result
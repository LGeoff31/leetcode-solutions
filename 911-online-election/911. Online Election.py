class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.lst = [] # (timestamp, lastmax)
        self.dic = defaultdict(int)
        lastMax = -1
        largest_freq = 0
        for i, t in enumerate(self.times):
            self.dic[persons[i]] += 1
            if self.dic[persons[i]] >= largest_freq:
                lastMax = persons[i]
                largest_freq = self.dic[persons[i]]
            self.lst.append((t, lastMax))
        print(self.lst)
    def q(self, t: int) -> int:
        idx = bisect_right(self.lst, (t, 1e9))-1
        return self.lst[idx][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
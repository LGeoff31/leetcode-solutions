class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1, odd1 = defaultdict(int), defaultdict(int)
        even2, odd2 = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            if i % 2 == 0:
                even1[s1[i]] += 1
                even2[s2[i]] += 1
            else:
                odd1[s1[i]] += 1
                odd2[s2[i]] += 1

        return odd1 == odd2 and even1 == even2


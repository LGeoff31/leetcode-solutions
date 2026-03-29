class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even1, odd1 = set(), set()
        even2, odd2 = set(), set()
        for i in range(4):
            if i % 2 == 0:
                even1.add(s1[i])

                even2.add(s2[i])
            else:
                odd1.add(s1[i])
                odd2.add(s2[i])
        return odd1 == odd2 and even1 == even2


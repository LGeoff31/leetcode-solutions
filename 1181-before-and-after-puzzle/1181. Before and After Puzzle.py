class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        n = len(phrases)
        def match(i, j):
            return phrases[i].split()[-1] == phrases[j].split()[0] and i != j
        res = []
        for i in range(n):
            for j in range(n):
                if match(i, j):
                    print('reached')
                    idx = phrases[j].index(" ") + 1 if " " in phrases[j] else len(phrases[j])
                    res.append(phrases[i] + (" " if idx != len(phrases[j]) else "") +  phrases[j][idx :])
        return sorted(list(set(res)))

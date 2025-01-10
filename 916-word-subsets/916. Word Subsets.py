class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        dic = defaultdict(int)
        for word in words2:
            a = defaultdict(int)
            for c in word:
                a[c] += 1
            for key in a:
                dic[key] = max(dic[key], a[key])
        print(dic)
        for word in words1:
            valid = True
            a = Counter(word)
            for key in dic:
                if key not in a: valid = False
                if dic[key] > a[key]: valid = False
            if valid:
                res.append(word)
        return res

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0 
        dic = defaultdict(list)
        for word in words:
            dic[word[0]].append(word[1:])
        
        for c in s:
            tmp = dic[c]
            dic[c] = [] # restart
            for w in tmp:
                if not w: 
                    res += 1
                else:
                    dic[w[0]].append(w[1:])
        return res
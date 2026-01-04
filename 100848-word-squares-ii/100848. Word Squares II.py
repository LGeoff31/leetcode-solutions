class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res = []
        def valid(i, j, k, l):
            top, left, right, bottom = words[i], words[j], words[k], words[l]
            return top[0] == left[0] and top[3] == right[0] and bottom[0] == left[3] and bottom[3] == right[3]
        for i in range(len(words)):
            for j in range(len(words)):
                for k in range(len(words)):
                    for l in range(len(words)):
                        if len({i,j,k,l}) == 4 and valid(i, j, k, l):
                            res.append([words[i], words[j], words[k], words[l]])
        res.sort()
        return res
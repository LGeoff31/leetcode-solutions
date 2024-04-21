class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        dic = defaultdict(list)
        for i, letter in enumerate(word):
            dic[letter].append(i)
        visited = set()
        for i in range(len(word)):
            if word[i] not in visited and word[i].lower() == word[i] and word[i].upper() in dic and dic[word[i].upper()][0] > dic[word[i]][-1]: 
                visited.add(word[i])
                res+=1
        return res
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        dic = {}
        for word in wordDict:
            dic[word] = len(word)

        def dfs(word, string, length): 
            if length == len(s):
                res.append(string)
            for i in range(1, 11):
                if len(word) < i: break
                if word[0:i] in dic:  #(i-1) is last index of word
                    print(word[0:i], word[i:], length + len(word[0:i]), string + word[0:i])
                    if len(word[i:]) == 0: dfs(word[i:], string + word[0:i], length + len(word[0:i]))
                    else: dfs(word[i:], string + word[0:i] + ' ', length + len(word[0:i]))

        for i in range(len(s)):
            dfs(s[i:], "", 0)
        return res
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # 1) longest 2) lexographically
        # lst = [Counter(word) for word in dictionary]
        dic = Counter(s)
        def valid(word):
            l, r = 0, 0
            while l < len(s) and r < len(word):
                if s[l] == word[r]:
                    l += 1
                    r += 1
                else:
                    l += 1
            return r == len(word)

        valid_lst = [word for word in dictionary if valid(word)]
        if not valid_lst: return ""
        print(valid_lst)
        maxLength = max(len(word) for word in valid_lst)
        new_lst = []
        print(valid_lst, maxLength)
        for word in valid_lst:
            if len(word) == maxLength:
                new_lst.append(word)
        new_lst.sort()
        if not new_lst: return ""
        return new_lst[0]
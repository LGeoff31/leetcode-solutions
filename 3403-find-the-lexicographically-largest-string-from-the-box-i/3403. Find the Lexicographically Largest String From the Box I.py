class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: return word
        # Find the largest letter in word and start from it
        largest_letter = max(word)
        idx = []
        for i in range(len(word)):
            if word[i] == largest_letter:
                idx.append(i)
        # Start from each of the largest letter indexes and you can traverse an additional numFriends letters
        n = len(word)
        res = ""
        for i in idx:
            curr = ""
            a = i
            while a < len(word) and n - len(curr) > numFriends-1:
                curr += word[a]
                a += 1
            if curr > res:
                res = curr
        return res
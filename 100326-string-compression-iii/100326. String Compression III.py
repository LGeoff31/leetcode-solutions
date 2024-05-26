class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        word += "~"

        prev = word[0]
        count = 1
        for i in range(1, len(word)):
            if word[i] == prev:
                count += 1
                if count == 10:
                    res += str(count-1) + prev
                    count = 1
            else:
                res += str(count)+prev
                prev = word[i]
                count = 1
        return res


        
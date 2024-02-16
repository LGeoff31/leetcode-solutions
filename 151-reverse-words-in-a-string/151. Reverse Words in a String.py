class Solution:
    def reverseWords(self, s: str) -> str:
        newString = ""
        for word in s.split()[::-1]:
            newString += word + " "

        return newString[:len(newString)-1]
        
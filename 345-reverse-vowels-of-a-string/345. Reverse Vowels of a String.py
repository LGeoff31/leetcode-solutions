class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        vowelSet = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for letter in s:
            if letter in vowelSet:
                vowels.append(letter)
        vowels = vowels[::-1]
        curr_idx = 0
        newString = ""
        for i in range(len(s)):
            if s[i] in vowelSet:
                newString += vowels[curr_idx]
                curr_idx += 1
            else:
                newString += s[i]
        return newString
        
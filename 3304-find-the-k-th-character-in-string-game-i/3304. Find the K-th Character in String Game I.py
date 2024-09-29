class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            new_string = ""
            for i in range(len(word)):
                new_string += chr((ord(word[i]) + 1) % 97 + 97)
            word += new_string
            print(word)
        return word[k-1]
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # The amount of elements in output must equal the length of the word (length 4 => 4 words)
        res = []
        # Brute force; Generate all possibilities of size 4 O(n^4), see if valid word O(4 * 4)
        n = len(words[0])
        def getPrefix(prefix):
            for word in words:
                if word.startswith(prefix):
                    yield word
        def backtrack(step, word_squares, res):
            if step == n:
                res.append(word_squares[:])
                return
            prefix = "".join(word[step] for word in word_squares)
            for candidate in getPrefix(prefix):
                word_squares.append(candidate)
                backtrack(step + 1, word_squares, res)
                word_squares.pop()
        for word in words:
            word_squares = [word]
            backtrack(1, word_squares, res)
        return res
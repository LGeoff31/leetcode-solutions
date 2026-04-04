class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        """
        s b s
        s a c
        """
        n = len(encodedText)
        cols = n // rows
        lst = [[""] * cols for _ in range(rows)]
        for i in range(len(encodedText)):
            r = i // cols
            c = i % cols
            lst[r][c] = encodedText[i]
        print(lst)
        res = ""
        for c in range(cols):
            # if lst[0][c] == "": break
            i = 0
            while i < len(lst) and c+i < len(lst[i]):
                res += lst[i][i+c]
                i += 1
        return res.rstrip()



        return ""
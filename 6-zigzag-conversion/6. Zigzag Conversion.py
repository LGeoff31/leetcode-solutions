class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [["a"] for _ in range(len(s))]
        print('res', res)
        down = True
        currRow = 0
        rowCounter = [0 for _ in range(numRows)]
        rowCounter2 = [0 for _ in range(numRows)]

        if numRows == 1:
            return s
        for i in range(len(s)):
            rowCounter[currRow] += 1
            if down:
                currRow += 1
                if currRow == numRows:
                    currRow = numRows - 2
                    down = False
            else:
                currRow -= 1
                if currRow == -1:
                    currRow = 1
                    down = True
        down = True
        curr = 0
        currRow = 0
        for i in range(len(s)):
            print(currRow, curr)
            res[sum(rowCounter[:currRow]) + rowCounter2[currRow]] = s[i]
            rowCounter2[currRow] += 1
            if down:
                currRow += 1
                if currRow == numRows:
                    currRow = numRows - 2
                    down = False
                    curr += 1
            else:
                currRow -= 1
                if currRow == -1:
                    currRow = 1
                    down = True
                    curr += 1

        print(rowCounter)
        print(res)

        return "".join(res)
                

        # res = ''
        # col = 0
        # while col < len(s):
        #     for i in range(numRows):
        #         res += s[col][i]
        #     for i in range(numRows - 1):
        #         col += 1
        #         if col >= len(s):
        #             return res
        #         res += s[col][i]

        # return res
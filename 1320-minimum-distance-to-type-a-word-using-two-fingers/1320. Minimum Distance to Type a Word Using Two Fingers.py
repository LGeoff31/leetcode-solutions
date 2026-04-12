# dp[i][j]=min cost after typing word[i], with the OTHER finger at j
# 26 denotes hovering
class Solution:
    def minimumDistance(self, word: str) -> int:
        dic = {
            "A": (0, 0), "B": (0,1), "C": (0, 2), "D": (0, 3), "E": (0, 4), "F": (0, 5),
            "G": (1, 0), "H": (1,1), "I": (1, 2), "J": (1, 3), "K": (1, 4), "L": (1, 5),
            "M": (2, 0), "N": (2,1), "O": (2, 2), "P": (2, 3), "Q": (2, 4), "R": (2, 5),
            "S": (3, 0), "T": (3,1), "U": (3, 2), "V": (3, 3), "W": (3, 4), "X": (3, 5),
            "Y": (4, 0), "Z": (4,1)
        }

        def dist(letter1, letter2):
            return abs(dic[letter1][0] - dic[letter2][0]) + abs(dic[letter1][1] - dic[letter2][1])
        @cache
        def dfs(i, prev1, prev2):
            if i == len(word):
                return 0

            res = 1e9
            # put prev1
            if not prev1:
                res = min(res, dfs(i+1, word[i], prev2))
            else:
                res = min(res, dist(prev1, word[i]) + dfs(i+1, word[i], prev2))
            
            # put prev2
            if not prev2:
                res = min(res, dfs(i+1, prev1, word[i]))
            else:
                res = min(res, dfs(i+1, prev1, word[i]) + dist(prev2, word[i]))
            return res


        return dfs(0, None, None)

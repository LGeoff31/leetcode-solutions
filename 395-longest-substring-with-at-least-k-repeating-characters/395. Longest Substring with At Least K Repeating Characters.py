class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(string): # This dfs will be called at most 26 times
            if not string:
                return 0
            indicies = defaultdict(list)
            for i, c in enumerate(string):
                indicies[c].append(i)

            frequency = Counter(string)
            invalidChar = ""
            for char in frequency:
                if frequency[char] < k:
                    invalidChar = char
                    break
            if invalidChar == "":
                return len(string)

            indexes = indicies[invalidChar]
            # leftMost = string[: start]
            # rightMost = string[end+1 : ]
            res = 0
            res = max(res, dfs(string[: indexes[0]]))
            res = max(res, dfs(string[indexes[-1]+1 : ]))
            for idx in range(1, len(indexes)):
                start, end = indexes[idx-1], indexes[idx]
                res = max(res, dfs(string[start + 1: end]))
            # start, end = indicies[invalidChar]

            # print(string, leftMost, rightMost, start, end)
            return res


        return dfs(s)
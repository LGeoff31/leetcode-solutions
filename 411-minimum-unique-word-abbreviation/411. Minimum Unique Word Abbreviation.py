class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        # Brute Force: Generate every single abbreviation of target, pick the smallest that doesn't exist in dictionary
        self.lst = []
        def dfs(idx, curr_abbreviated, currString):
            if idx == len(target):
                # print('reached', idx, curr_abbreviated, currString)
                if curr_abbreviated > 0:
                    currString += str(curr_abbreviated)
                self.lst.append(currString)
                return
            
            # TAKE THE LETTER
            dfs(idx+1, 0, currString + (str(curr_abbreviated) if curr_abbreviated != 0 else "") + target[idx])
            # DONT TAKE, ABBREVIATE
            dfs(idx+1, curr_abbreviated + 1, currString)
            
        dfs(0, 0, "")
        # print(self.lst)
        # print("a10" in self.lst)
        # dictionary_set = set(dictionary)
        def match(abbr, word):
            # If abbr can be made into word, return True, otherwise False
            i, j = 0, 0
            while i < len(abbr) and j < len(word):
                if abbr[i].isdigit():
                    # Extract the entire digit, note that abbr[i] cannot be 0 by the way its constructed
                    num = ""
                    while i < len(abbr) and abbr[i].isdigit():
                        num += abbr[i]
                        i += 1
                    j += int(num)
                else:
                    if abbr[i] == word[j]:
                        i += 1
                        j += 1
                    else:
                        return False
            return i == len(abbr) and j == len(word)
        def length(string):
            res = 0
            idx = 0
            while idx < len(string):
                if string[idx].isdigit():
                    while idx < len(string) and string[idx].isdigit():
                        idx += 1
                    res += 1
                else:
                    res += 1
                    idx += 1
            return res
        res = "a" * len(target)
        for abbr in self.lst:
            valid = True
            for word in dictionary:
                if match(abbr, word):
                    valid = False
            if valid:
                if length(abbr) <= length(res):
                    res = abbr
        return res
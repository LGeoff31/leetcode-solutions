class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {}
        dic[2] = ["a","b","c"]
        dic[3] = ["d","e","f"]
        dic[4] = ["g","h","i"]
        dic[5] = ["j","k","l"]
        dic[6] = ["m","n","o"]
        dic[7] = ["p","q","r", "s"]
        dic[8] = ["t","u", "v"]
        dic[9] = ["w","x", "y", "z"]
        if not digits:
            return []
        res = []
        curr_string = ""
        def dfs(i, curr_string):
            if i >= len(digits):
                res.append(curr_string)
                return
            
            for letter in dic[int(digits[i])]:
                curr_string += letter
                dfs(i+1, curr_string)
                curr_string = curr_string[0:len(curr_string)-1]
        
        dfs(0, "")

        return res




        
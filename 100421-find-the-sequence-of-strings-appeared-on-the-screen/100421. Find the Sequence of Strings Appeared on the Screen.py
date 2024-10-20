class Solution:
    def stringSequence(self, target: str):
        # Start with an initial string "a"
        curr = "a"
        result = ["a"]
        
        for i in range(len(target)):
            while len(curr) <= i:
                curr += "a"
                result.append(curr)
            
            while curr[-1] != target[i]:
                curr = curr[:-1] + chr(ord(curr[-1]) + 1)
                result.append(curr)
        
        return result
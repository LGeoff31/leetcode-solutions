class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        res = 0
        i = 0
        visited = set()
        while i < len(instructions) and i >= 0:
            if i in visited: 
                break
            visited.add(i)
            if instructions[i] == "add":
                res += values[i]
                i += 1
            else:
                i += values[i]
            # i += 1
            print(res, i)
                
        return res
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        visited = set()
        def shift(string):  
            visited.add(string)
            old_string = string
            string = string[1:] + string[0]
            visited.add(string)
            while string != old_string:
                string = string[1:] + string[0]
                visited.add(string)
            visited.add(string)
        
        shift(s)
        print(visited)
        return goal in visited
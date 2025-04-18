class Solution:
    def countAndSay(self, n: int) -> str:
        currString = "1"
        def convert(string):
            i = 0
            new_string = ""
            while i < len(string):
                curr_freq = 1
                curr_char = string[i]
                while i+1 < len(string) and string[i+1] == string[i]:
                    curr_freq += 1
                    i += 1
                else:
                    i += 1
                new_string += str(curr_freq) + curr_char 
            return new_string
        for i in range(n-1):
            currString = convert(currString)
            print(currString)
        return currString
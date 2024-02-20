class Solution:
    def compress(self, chars: List[str]) -> int:    
        ans, idx = 0, 1
        prevChar = chars[0]
        count = 1
        while idx < len(chars):
            currChar = chars[idx]
            if currChar == prevChar:
                count += 1
            else:
                chars[ans] = prevChar
                if count != 1:
                    print(count)
                    for character in str(count):
                        ans += 1
                        chars[ans] = character
                    # ans += 1
                    # chars[ans] = str(count)
                    count = 1
                ans += 1
            prevChar = currChar
            idx += 1
        chars[ans] = prevChar
        # chars[ans] = prevChar 
        print(count, chars, ans)
        if count != 1:
            for character in str(count):
                ans += 1
                chars[ans] = character


        return ans+1



        
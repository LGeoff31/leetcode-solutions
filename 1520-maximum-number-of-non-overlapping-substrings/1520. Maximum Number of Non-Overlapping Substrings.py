class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i
        
        intervals = []
        for c in range(26):
            if last[c] == -1:
                continue 
            
            l, r = first[c], last[c]
            valid = True

            i = l
            while i <= r:
                x = ord(s[i]) - ord('a')
                if first[x] < l:
                    valid = False
                    break
                r = max(r, last[x])
                i += 1
            if valid:
                intervals.append((r, l))
        intervals.sort()

        ans = []
        prevEnd = -1
        for r, l in intervals:
            if l > prevEnd:
                ans.append(s[l : r+1])
                prevEnd = r
        return ans
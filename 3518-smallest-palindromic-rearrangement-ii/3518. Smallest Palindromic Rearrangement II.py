class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:

        mid = ""
        if len(s) % 2 == 1:
            mid = s[len(s)//2]
        #middle character can't be moved elsewhere
        
        cnt = [0]*26
        for i in range(len(s)):
            if len(s)%2 == 1 and i == len(s)//2:
                continue
            val = ord(s[i])-ord("a")
            cnt[val] += 1

        #only need half the counts since we'll form first half, then second half is mirrored
        for i in range(len(cnt)):
            cnt[i] //= 2

        out = []
        
        for i in range(len(s)//2):
            for j in range(len(cnt)):
                #try first available char
                if cnt[j] > 0:
                    cnt[j] -= 1 #use this as next char

                    ways = 1
                    letters = sum(cnt)
                    for freq in cnt:
                        if freq > 0:
                            #do this to divide out repeat letter combinations
                            ways *= math.comb(letters, freq)
                            letters -= freq
                        if ways >= k: #avoid computing large numbers over k
                            break
                    
                    if ways >= k:
                        out.append(chr(ord("a")+j))
                        break
                    
                    #update ways we've passed
                    k -= ways
                    cnt[j] += 1 #add back to count if this isn't next char

            #no valid
            else:
                return ""
                
        #how many ways to arrange first half, then fill in rest
        out = "".join(out)
        return out + mid + out[::-1]
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        """
        0 will always be binary palindromic
        the rest should NEVER start with a 0 (since no leading 0's)
        TLE -> loop up to N
        Is there a special property regarding binary palindromes??? 1's must be fixed, so it goes down to some combinatorics (n-2)
        LENGTH 1: 0, 1
        LENGTH 2: 11
        LENGTH 3: 101, 111
        LENGTH 4: 1001, 1111 
        LENGTH 5: 10001, 10101, 11011, 11111

        Key observation: let's say we have full freedom of binary of length x.
        If x is odd, we can look at first less than half and pick any 1's or 0's so 2^(floor(x/2)) then multiply by 2 since middle 0/1
        if x is even, we can do 2^(floor(x/2))
        Can be simplified if restriced by leading and trailing 1, to ceil(x/2) - 1

        We can do some binary searching!?/!?
        10^15 -> ~50 binary bits
        """
        n_length = len(bin(n)[2:])
        # ALL binary rep's with length < n_length can be included saftely without being > n
        res = 1 # bc 0
        for i in range(1, n_length):
            res += 2 ** (ceil(i/2) - 1)
        # now for binary length == n, we want to count up so that it doesn't exceed n
        first_half = (n_length+1) // 2
        b = bin(n)[2:]
        endpoint = (len(b) + 1) // 2
            
        target = b[: endpoint]
        @cache
        def dfs(idx, good):
            if idx >= len(target):
                return 1
            ans = 0
            if good:
                if idx == 0:
                    if target[idx] == "1":
                        ans += dfs(idx + 1, True)
                else:
                    if target[idx] == "1":
                        ans += dfs(idx + 1, True) # placing a 1
                        ans += dfs(idx + 1, False) # Place a 0
                    else:
                        ans += dfs(idx+1, True) # Placing a 0
            else:
                if idx == 0:
                    ans += dfs(idx + 1, False)
                else:
                    ans += dfs(idx + 1, False)
                    ans += dfs(idx+1, False)
            return ans
        res += dfs(0, True)
        s = target
        if n_length % 2 == 0:
            pal = s + s[::-1]
        else:
            pal = s + s[-2::-1]
        if int(pal, 2) > n:
            res -= 1
        return res
        
        # DFS??!?
        
        

        
        
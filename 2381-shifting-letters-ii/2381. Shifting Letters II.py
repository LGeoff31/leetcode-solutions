class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * len(s)
        for x,y,z in shifts:
            if z == 0: z = -1
            prefix[y] += z
            if x != 0:
                prefix[x-1] -= z
        for i in range(len(prefix) - 2, -1, -1):
            prefix[i] += prefix[i+1]
        lst = [ord(letter) - ord("a") for letter in s]
        for i in range(len(prefix)):
            lst[i] = (lst[i] + prefix[i]) % 26  

        return "".join(list(chr(i+97) for i in lst))

            
        
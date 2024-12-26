class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        lst = [(8-len(bin(num)[2:])) * "0" + bin(num)[2:] for num in data]
        i = 0
        print(lst)
        while i < len(lst):
            numBytes = 0
            for char in lst[i]:
                if char == "1": numBytes += 1
                else: break
            print(numBytes)
            if not(numBytes == 0 or numBytes == 2 or numBytes == 3 or numBytes == 4): return False
            if numBytes == 0: numBytes = 1
            for nxtBytes in range(i+1, i + numBytes):
                # print(lst[nxtBytes])
                if nxtBytes >= len(lst): return False
                if lst[nxtBytes][:2] != "10": return False
            i = i + numBytes
        return True
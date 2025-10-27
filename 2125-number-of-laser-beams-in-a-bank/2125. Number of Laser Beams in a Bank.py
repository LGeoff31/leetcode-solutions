class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        new_bank = []
        for arr in bank:
            if arr.count("1") == 0:
                continue
            new_bank.append(arr)
        bank=new_bank
        for i in range(len(bank) - 1):
            res += bank[i].count("1") * bank[i+1].count("1")
        return res
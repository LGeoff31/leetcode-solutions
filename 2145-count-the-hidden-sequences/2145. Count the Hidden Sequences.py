class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        if max(differences) < 0:
            lst = [upper]
            for diff in differences:
                lst.append(lst[-1] + diff)
            minElem = min(lst)

            return max(minElem - lower + 1, 0)
        # Versions will just be transalted versions of each other
        prefix = [0]+list(accumulate(differences))
        lst = [upper - max(prefix)]
        for diff in differences:
            lst.append(lst[-1] + diff)
        minElem = min(lst)

        return max(minElem - lower + 1, 0)

        # [3,-1,4,5,3]

        # [53, 13]
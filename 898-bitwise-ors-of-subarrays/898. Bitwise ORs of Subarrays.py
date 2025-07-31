class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        """
        OR'ing values only increases the value
        [1, 2, 4, 8] -> 15 since 1111, can't be 0

        [1,2,4,7,9]

        we know 1,2,4 covers 1,2,3,...,7

        now we come across 7, we can add all these 7 values
        now we come across 9, we can add all these 7 values

        but we need to subtract the overlap

        [2,4,7,9]

        1) remove dups

        """
        cur = set()
        res = set()
        prevCur = set()

        lst = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] != lst[-1]:
                lst.append(arr[i])
        for i in range(len(lst)):
            cur.add(lst[i])
            for key in prevCur:
                cur.add(key | lst[i])
            for key in cur:
                res.add(key)
            prevCur = cur
            cur = set()
            
        return len(res)


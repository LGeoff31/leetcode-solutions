class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        res = []
        pairs = {}
        for pair in adjacentPairs:
            if pair[0] not in pairs:
                pairs[pair[0]] = [pair[1]]
            else:
                pairs[pair[0]].append(pair[1])

            if pair[1] not in pairs:
                pairs[pair[1]] = [pair[0]]
            else:
                pairs[pair[1]].append(pair[0])
        for key, val in pairs.items():
            if len(val) == 1:
                res.append(key)
                res.append(val[0])
                break
        while True:
            array = pairs[res[-1]]
            second_last_elem = res[-2]
            if len(array) == 1:
                break
            if array[0] != second_last_elem:
                res.append(array[0])
            else:
                res.append(array[1])
        return res

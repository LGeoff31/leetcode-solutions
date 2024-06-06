class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()

        dic = Counter(hand)
        idx = 0
        #[1,2,2,3,3,4,6,7,8]
        #[1,2,3,4,6,7,8], 3
        #{2:1, 3:1, 4:1, 6:1, 7:1, 8:1}
        unique = sorted(list(set(hand)))
        print("unique", unique)
        while idx < len(unique):
            for i in range(groupSize):
                if unique[idx] + i not in dic:
                    return False
                dic[unique[idx]+i] -= 1
                if dic[unique[idx] + i] == 0:
                    del dic[unique[idx] + i]
                # print(dic)
                # break
            # print(dic)
            while idx < len(unique) and unique[idx] not in dic:
                idx+=1
            # if unique[idx] not in dic:
                # idx += 1
            # print(idx)
            # break
            

        return True
        
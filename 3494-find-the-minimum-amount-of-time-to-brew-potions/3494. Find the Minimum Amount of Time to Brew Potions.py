class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        """
        0   |   5   |   30  |   40  |   60
        x   |   x+1 |   x+6 |   x+8 |   x+12

        get following
        x=5
        x=29
        x=34
        x=52

        pick the largest x
        """
        base = [0] + list(accumulate([skill[i]*mana[0] for i in range(len(skill))]))
        # print(base)
        for i in range(1, len(mana)):
            nxt_lst = []
            acc = 0
            for j in range(len(skill)):
                nxt_lst.append(base[j+1] - acc)
                acc += mana[i] * skill[j]
            x = max(nxt_lst)
            base = list(accumulate([x] + [skill[j]*mana[i] for j in range(len(skill))]))
            # base.append(base[-1] + mana[i] * skill[-1])
            # print(base)
            # nxt_lst.append(nxt_lst[-1] + mana[i] * skill[-1])

            # print(nxt_lst)
            # base=nxt_lst
        return base[-1]
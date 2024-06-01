class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        res = [[None]] * len(people)
        # print(people)
        # print(res)
        for i in range(len(people)):
            jumps = people[i][1]
            idx = 0
            while idx < len(res) and jumps != 0:
                if len(res[idx]) == 1:
                    # print("reached")
                    jumps -= 1
                elif res[idx][0] == people[i][0]:
                    jumps -= 1
                idx+=1
            while idx < len(res):
                if len(res[idx]) == 2:
                    idx+=1
                else:
                    break

            res[idx] = people[i]
            # print(res)
        return res
        
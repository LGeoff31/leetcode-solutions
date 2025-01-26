class Solution:
    def findContestMatch(self, n: int) -> str:  
        lst = list(range(1, n+1)) # [1,2,3,4,5,6,7,8]
        rounds = int(math.log2(n))
        for i in range(rounds):
            new_lst = []
            for j in range(len(lst) // 2):
                new_lst.append("(" + str(lst[j]) + "," + str(lst[len(lst) - j - 1]) + ")")
            lst = new_lst
            print(lst)
        return lst[0]
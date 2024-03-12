class Solution:
    def candy(self, ratings: List[int]) -> int:
        lst = [1] * len(ratings)

        #forward
        for i in range(len(ratings)-1):
            if ratings[i] < ratings[i+1]:
                lst[i+1] = lst[i] + 1
        #backward
        print(lst)
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i] < ratings[i-1] and lst[i-1] <= lst[i]:
                lst[i-1] = lst[i] + 1
        print(lst)
        return sum(lst)


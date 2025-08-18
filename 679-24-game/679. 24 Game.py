class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def getResults(a,b):
            lst = [a+b, a-b, b-a, a*b]
            if b: lst.append(a/b)
            if a: lst.append(b/a)
            return lst
        def backtrack(arr):
            if len(arr) == 1:
                return abs(arr[0]-24) <= 0.01

            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    new_arr = [number for k,number in enumerate(arr) if i!=k and j!=k]
                    # Added all numbers except the pair

                    for res in getResults(arr[i], arr[j]):
                        # new_arr.append(res)
                        if backtrack(new_arr + [res]):
                            return True
                        # new_arr.pop()
            return False
        return backtrack(cards)
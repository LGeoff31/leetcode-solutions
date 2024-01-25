class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lst = []

        def permutation(string, acc):
            # base case
            if len(string) == 0:
                lst.append(acc)
                return
            for i in range(len(string)):
                new_acc = acc + string[i]
                if i == 0:
                    new_string = string[1:]
                elif i == len(string) - 1:
                    new_string = string[:len(string)-1]
                else:
                    new_string = string[0:i] + string[i+1:]
                permutation(new_string, new_acc)
        permutation(s1, "")
        for word in lst:
            if word in s2:
                return True
        return False
